# Bluesky firehose consumer

The Worker in `worker.py` upgrades incoming requests to WebSocket connections and
streams messages from the public Bluesky firehose down to the client. The example
shows how to use the WebSocket APIs in Python Workers to consume data from external
servers while proxying it to clients.

> **Note**
> The Bluesky firehose is a high-volume stream. Consider filtering messages or
> throttling output before using this pattern in production.

## Usage

1. Copy `worker.py` into your Worker project.
2. Run `wrangler dev` and connect with a WebSocket client (for example using
   `wscat` or your own frontend) to observe the incoming firehose events.
