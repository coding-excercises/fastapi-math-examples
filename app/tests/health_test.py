from app.api.health_fn import health_func


def test_func_health() -> None:
    result = health_func()
    assert result == "ok"