"""Generate images on the fly using Pillow."""
from __future__ import annotations

from datetime import datetime
from io import BytesIO
from urllib.parse import urlparse

from PIL import Image, ImageDraw
from workers import Response, WorkerEntrypoint


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        """Render a simple social card containing the current timestamp."""
        width, height = 600, 315
        background = getattr(self.env, "CARD_BACKGROUND", "#1e293b")
        accent = getattr(self.env, "CARD_ACCENT", "#38bdf8")

        image = Image.new("RGB", (width, height), background)
        draw = ImageDraw.Draw(image)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        path = urlparse(request.url).path or "/"

        draw.rectangle([(40, 40), (width - 40, height - 40)], outline=accent, width=6)
        draw.text((60, 80), "Dynamic Pillow Image", fill="white")
        draw.text((60, 160), f"Path: {path}", fill="#e2e8f0")
        draw.text((60, 210), f"Generated at: {timestamp}", fill="#e2e8f0")

        buffer = BytesIO()
        image.save(buffer, format="PNG")

        return Response(buffer.getvalue(), headers={"content-type": "image/png"})
