# Pillow image generator

This Worker uses the Pillow package to render a PNG image every time it receives a
request. The example produces a simple 600x315 card that includes the requested path
and the current timestamp.

## Usage

1. Add `Pillow` to the project's `requirements.txt`.
2. Copy `worker.py` into your Worker project.
3. Run `wrangler dev` and visit the Worker URL to download the generated image.
4. Adjust the colors by defining `CARD_BACKGROUND` and `CARD_ACCENT` environment
   variables if desired.
