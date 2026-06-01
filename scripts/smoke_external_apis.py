"""User-triggered external API smoke tests with redacted output only."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from modules.api_clients import (
    fetch_bus_arrival,
    fetch_bus_route,
    fetch_weather_short_forecast,
    test_vworld_geocode_connection,
)
from modules.emailer import email_status
from modules.llm_client import test_openrouter_text_connection
from modules.vision import test_vision_model_available


def _safe_result(name: str, fn: Callable[[], dict[str, Any]]) -> dict[str, Any]:
    try:
        result = fn()
    except Exception as exc:
        result = {
            "status": "script_error",
            "reason": exc.__class__.__name__,
            "source": "smoke_script",
        }
    return {
        "name": name,
        "ok": bool(result.get("ok", result.get("status") in {"real_api", "real_api_no_data", "configured"})),
        "status": result.get("status", result.get("data_status", "unknown")),
        "source": result.get("source", ""),
        "reason": result.get("reason_code", result.get("reason", "")),
        "action_needed": result.get("action_needed", ""),
        "real_count": result.get("real_count", ""),
        "fallback_count": result.get("fallback_count", ""),
    }


def main() -> None:
    checks: list[tuple[str, Callable[[], dict[str, Any]]]] = [
        ("VWorld geocode", lambda: test_vworld_geocode_connection("운양역")),
        ("Weather forecast", fetch_weather_short_forecast),
        ("TAGO bus route", lambda: fetch_bus_route(route_no="81")),
        ("TAGO bus arrival", lambda: fetch_bus_arrival(route_no="81")),
        ("OpenRouter text", test_openrouter_text_connection),
        ("Vision model", test_vision_model_available),
        ("SendGrid status", email_status),
    ]
    for name, fn in checks:
        row = _safe_result(name, fn)
        print(
            "\t".join(
                f"{key}={row[key]}"
                for key in ("name", "ok", "status", "source", "reason", "action_needed", "real_count", "fallback_count")
            )
        )


if __name__ == "__main__":
    main()
