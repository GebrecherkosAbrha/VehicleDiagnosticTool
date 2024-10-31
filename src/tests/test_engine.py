import pytest
from components.engine import Engine


@pytest.fixture
def engine():
    return Engine()


def test_high_temperature(engine):
    data = {'engine_temperature': 125, 'oil_level': 50}
    issues = engine.diagnose(data)
    assert "Engine temperature is too high (125°C)" in issues


def test_low_oil_level(engine):
    data = {'engine_temperature': 80, 'oil_level': 15}
    issues = engine.diagnose(data)
    assert "Oil level is low (15%)" in issues


def test_normal_conditions(engine):
    data = {'engine_temperature': 90, 'oil_level': 70}
    issues = engine.diagnose(data)
    assert not issues
