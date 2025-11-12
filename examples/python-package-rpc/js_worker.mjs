// Call a Python Worker over RPC to reuse a Python package from JavaScript.
export default {
  async fetch(request, env) {
    const now = new Date().toISOString();
    const payload = { timestamp: now, tz: "America/New_York" };
    const result = await env.TIME_API.rpc.convert_timezone(payload);

    return new Response(
      JSON.stringify({ input: payload, converted: result }, null, 2),
      {
        headers: {
          "content-type": "application/json; charset=utf-8",
        },
      },
    );
  },
};
