"""Dynamic OpenGraph tag injection example."""
from html import escape
from urllib.parse import urlparse

from workers import Response, WorkerEntrypoint


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        """Return HTML with dynamic OpenGraph metadata for each path."""
        url = urlparse(request.url)
        slug = url.path.strip("/") or "home"

        titles = {
            "home": "Welcome to the Sample Site",
            "about": "About This Demo",
            "products": "Our Featured Products",
        }
        descriptions = {
            "home": "A minimal Cloudflare Python Worker injecting OpenGraph tags dynamically.",
            "about": "Learn how the Worker chooses metadata depending on the requested path.",
            "products": "Browse a curated list of fictional goods and see metadata updates automatically.",
        }

        title = titles.get(slug, f"Viewing {slug.title()} on Our Site")
        description = descriptions.get(slug, "Dynamic metadata keeps previews fresh across routes.")

        og_base = getattr(self.env, "OG_IMAGE_BASE", "https://example.com/assets")
        og_image = f"{og_base.rstrip('/')}/{slug}.png"
        canonical = f"https://example.com/{slug if slug != 'home' else ''}".rstrip("/")

        html = f"""<!doctype html>
<html lang=\"en\">
  <head>
    <meta charset=\"utf-8\" />
    <title>{escape(title)}</title>
    <meta name=\"description\" content=\"{escape(description)}\" />
    <meta property=\"og:title\" content=\"{escape(title)}\" />
    <meta property=\"og:description\" content=\"{escape(description)}\" />
    <meta property=\"og:url\" content=\"{escape(canonical)}\" />
    <meta property=\"og:image\" content=\"{escape(og_image)}\" />
  </head>
  <body>
    <main>
      <h1>{escape(title)}</h1>
      <p>{escape(description)}</p>
      <p>Requested slug: <code>{escape(slug)}</code></p>
    </main>
  </body>
</html>"""

        return Response(html, headers={"content-type": "text/html; charset=utf-8"})
