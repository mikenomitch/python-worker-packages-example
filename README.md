# FastAPI + Jinja2 Example

*Note: You must have Python Packages enabled on your account for built-in packages to work. Request Access to our Closed Beta using [This Form](https://forms.gle/FcjjhV3YtPyjRPaL8)*

This is an example of a Python Worker that uses a built-in package (FastAPI) with a vendored package (Jinja2).

## Additional examples

The `examples/` directory contains more sample Workers that highlight common patterns:

- **`examples/dynamic-opengraph/`** – Dynamically inject OpenGraph metadata into HTML responses.
- **`examples/durable-objects-chat/`** – Build a chat room backed by Durable Objects and WebSockets.
- **`examples/websocket-firehose/`** – Consume and proxy external WebSocket streams like the Bluesky firehose.
- **`examples/pillow-image/`** – Generate social preview images on demand with the Pillow package.
- **`examples/python-package-rpc/`** – Expose Python package functionality over RPC and call it from JavaScript.

Use these examples alongside the main project to explore different Python Worker capabilities.

## Adding Packages

Built-in packages can be selected from [this list](https://developers.cloudflare.com/workers/languages/python/packages/#supported-packages) and added to your `requirements.txt` file. These can be used with no other explicit install step.

Vendored packages are added to your source files and need to be installed in a special manner. The Python Workers team plans to make this process automatic in the future, but for now, manual steps need to be taken.

### Vendoring Packages

First, install Python3.12 and pip for Python 3.12.

*Currently, other versions of Python will not work - use 3.12!*

Then create a virtual environment and activate it from your shell:
```console
python3.12 -m venv .venv
source .venv/bin/activate
```

Within our virtual environment, install the pyodide CLI:
```console
.venv/bin/pip install pyodide-build
.venv/bin/pyodide venv .venv-pyodide
```

Next, add packages to your vendor.txt file. Here we'll add jinja2
```
jinja2
```

Lastly, add these packages to your source files at `src/vendor`. For any additional packages, re-run this command.
```console
.venv-pyodide/bin/pip install -t src/vendor -r vendor.txt
```

### Using Vendored packages

In your wrangler.toml, make the vendor directory available:

```toml
[[rules]]
globs = ["vendor/**"]
type = "Data"
fallthrough = true
```

Now, you can import and use the packages:

```python
import jinja2
# ... etc ...
```

### Developing and Deploying

To develop your Worker, run `wrangler dev`.

To deploy your Worker, run `wrangler deploy`.
