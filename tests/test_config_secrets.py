from __future__ import annotations

from modules.config import get_bool_secret, list_config_status
from modules.api_clients import get_data_go_kr_key


def test_list_config_status_reports_state_without_values(monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "secret-openrouter-value")
    monkeypatch.setenv("VWORLD_API_KEY", "secret-vworld-value")
    status = list_config_status()
    assert status["OPENROUTER_API_KEY"] == "configured"
    assert status["VWORLD_API_KEY"] == "configured"
    rendered = repr(status)
    assert "secret-openrouter-value" not in rendered
    assert "secret-vworld-value" not in rendered


def test_sendgrid_default_is_disabled(monkeypatch):
    monkeypatch.delenv("ENABLE_SENDGRID_SEND", raising=False)
    assert get_bool_secret("ENABLE_SENDGRID_SEND", False) is False
    monkeypatch.setenv("ENABLE_SENDGRID_SEND", "false")
    assert get_bool_secret("ENABLE_SENDGRID_SEND", False) is False
    monkeypatch.setenv("ENABLE_SENDGRID_SEND", "true")
    assert get_bool_secret("ENABLE_SENDGRID_SEND", False) is True


def test_data_go_key_decodes_once_without_logging(monkeypatch):
    monkeypatch.setenv("DATA_GO_KR_SERVICE_KEY", "abc%2Bdef%3D")
    assert get_data_go_kr_key() == "abc+def="
