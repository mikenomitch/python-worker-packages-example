# Access Python packages from JavaScript with RPC

This example uses two Workers:

- A Python Worker (`python_worker.py`) that imports the [`pendulum`](https://pypi.org/project/pendulum/)
  package and exposes a timezone conversion method over RPC.
- A JavaScript Worker (`js_worker.mjs`) that binds to the Python Worker and calls that method
  without re-implementing the logic in JavaScript.

## Usage

1. Deploy the Python Worker and add `pendulum` to its `requirements.txt`.
2. Configure a service binding for the JavaScript Worker:

   ```toml
   [[services]]
   binding = "TIME_API"
   service = "python-timezone-api"
   environment = "production"
   ```

3. In the JavaScript Worker, call `env.TIME_API.rpc.convert_timezone` to invoke the Python
   function. The response includes both the original input and the converted timestamp.
