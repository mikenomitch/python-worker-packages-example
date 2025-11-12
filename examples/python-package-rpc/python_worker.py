"""Expose Pendulum timezone conversions over RPC."""
from __future__ import annotations

import pendulum
from workers import WorkerEntrypoint


class TimezoneAPI(WorkerEntrypoint):
    async def rpc_convert_timezone(self, timestamp: str, tz: str = "UTC"):
        """Return timestamp information converted to the requested timezone."""
        dt = pendulum.parse(timestamp).in_timezone(tz)
        return {
            "iso": dt.to_iso8601_string(),
            "human": dt.format("YYYY-MM-DD HH:mm:ss ZZ"),
        }
