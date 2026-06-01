"""User-triggered external API smoke tests with redacted output only."""

from __future__ import annotations

from typing import Any

from engine_bridge import dashboard_api_status_items


FIELDS = ("name", "status", "source", "reason_code", "action_needed", "real_count", "fallback_count")


def _safe_text(value: Any) -> str:
    return str(value if value is not None else "")


def main() -> None:
    for row in dashboard_api_status_items(refresh=True):
        print("\t".join(f"{key}={_safe_text(row.get(key, ''))}" for key in FIELDS))


if __name__ == "__main__":
    main()
