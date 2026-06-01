"""Print safe configuration status without exposing secret values."""

from __future__ import annotations

from modules.config import list_config_status


def main() -> None:
    for name, status in list_config_status().items():
        print(f"{name}: {status}")


if __name__ == "__main__":
    main()
