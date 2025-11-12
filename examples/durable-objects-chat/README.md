# Durable Object chat room

This Worker demonstrates how Python Durable Objects can coordinate WebSocket
connections. Every client that connects through the Worker is forwarded to a
single Durable Object instance. The object accepts the WebSocket upgrade,
tracks the connection, and relays each message to all other connected peers.

## Usage

1. Update your `wrangler.toml` with a Durable Object binding:

   ```toml
   [[durable_objects.bindings]]
   name = "CHAT_ROOMS"
   class_name = "ChatRoom"
   ```

2. Copy `worker.py` into your project and register the Durable Object class.
3. Run `wrangler dev` and open multiple browser tabs pointing to the same Worker
   to verify that chat messages propagate to everyone.
