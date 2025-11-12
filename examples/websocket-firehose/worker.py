"""Consume data from a public WebSocket feed (Bluesky firehose)."""
from __future__ import annotations

import asyncio

from workers import Response, WebSocketPair, WorkerEntrypoint, connect

FIREHOSE_URL = "wss://bsky.network/xrpc/com.atproto.sync.subscribeRepos"


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        if request.headers.get("Upgrade", "").lower() != "websocket":
            return Response("Connect with a WebSocket client to stream Bluesky events.", status=400)

        pair = WebSocketPair()
        client, server = pair.client, pair.server
        await server.accept()

        upstream = await connect(FIREHOSE_URL)
        await upstream.accept()

        async def forward(source, target):
            async for message in source:
                await target.send(message)

        async def close_when_done():
            try:
                await asyncio.gather(
                    forward(upstream, server),
                    forward(server, upstream),
                )
            finally:
                await server.close()
                await upstream.close()

        asyncio.create_task(close_when_done())
        return Response(status=101, webSocket=client)
