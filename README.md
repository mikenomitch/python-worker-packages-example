# FastAPI + Jinja2 Example

This is an example of a Python Worker that uses a built-in package (FastAPI) with a vendored package (Jinja2).

## Adding Packages

Built-in packages can be selected from [this list](https://developers.cloudflare.com/workers/languages/python/packages/#supported-packages) and added to your `requirements.txt` file. These can be used with no other explicit install step.

Vendored packages are added to your source files and need to be installed in a special manner. The Python Workers team plans to make this process automatic in the future, but for now, manual steps need to be taken.

### Vendoring Packages

First, install Python3.12 and pip for Python 3.12.

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
```requirements.txt
jinja2
```

Lastly, add these packages to your source files at `src/vendor`. For any additional packages, re-run this command.
```console
.venv-pyodide/bin/pip install -t src/vendor -r vendor.txt
```

### Using Vendored packages

In your wrangler.toml, make the vendor directory available:

```toml
rules = [{ type = "Data", globs = ["vendor/**"], fallthrough = true }]
```

Now, you can import that directory in Python and use packages

```python
# Add the vendored libraries to the path
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent / "vendor"))

import jinja2

# ... etc ...
```
