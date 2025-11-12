# Dynamic OpenGraph Tag Injection

This example shows how you can tailor the HTML returned by your Python Worker based on
information in the incoming request. Every route chooses a title, description, and
OpenGraph image URL dynamically before returning the response.

## Usage

1. Copy `worker.py` into a new Worker project or set `main = "examples/dynamic-opengraph/worker.py"`
   in your `wrangler.toml`.
2. Optionally define an `OG_IMAGE_BASE` environment variable so the example can build fully
   qualified image URLs.
3. Start the Worker with `wrangler dev` and navigate to `/`, `/about`, or `/products` to see
   the metadata change.
