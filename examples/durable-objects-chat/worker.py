"""Durable Object powered WebSocket chat room."""
from __future__ import annotations

from typing import Set
from urllib.parse import urlparse

from workers import DurableObject, DurableObjectNamespace, Response, WebSocket, WebSocketPair, WorkerEntrypoint


class ChatRoom(DurableObject):
    """Durable Object that fans chat messages out to every connected client."""

    def __init__(self, ctx, env):
        super().__init__(ctx, env)
        self.clients: Set[WebSocket] = set()

    async def fetch(self, request):
        if request.headers.get("Upgrade", "").lower() != "websocket":
            return Response("Upgrade to WebSocket to join the chat", status=400)

        pair = WebSocketPair()
        client, server = pair.client, pair.server
        await server.accept()
        self.clients.add(server)

        async def pump() -> None:
            try:
                async for message in server:
                    for peer in list(self.clients):
                        try:
                            await peer.send(message)
                        except Exception:
                            self.clients.discard(peer)
            finally:
                self.clients.discard(server)

        self.ctx.wait_until(pump())
        return Response(status=101, webSocket=client)


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        url = urlparse(request.url)
        namespace: DurableObjectNamespace = self.env.CHAT_ROOMS
        room_name = url.path.strip("/") or "lobby"
        stub = namespace.get(namespace.id_from_name(room_name))
        return await stub.fetch(request)
