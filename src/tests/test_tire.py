import pytest
from components.tire import Tire


@pytest.fixture
def tire():
    return Tire()


def test_low_pressure(tire):
    data = {'tire_pressure': 25, 'tire_tread_depth': 8}
    issues = tire.diagnose(data)
    assert "Tire pressure is low (25 PSI)" in issues


def test_high_pressure(tire):
    data = {'tire_pressure': 40, 'tire_tread_depth': 8}
    issues = tire.diagnose(data)
    assert "Tire pressure is high (40 PSI)" in issues


def test_low_tread_depth(tire):
    data = {'tire_pressure': 32, 'tire_tread_depth': 2}
    issues = tire.diagnose(data)
    assert "Tire tread depth is low (2 mm)" in issues


def test_normal_conditions(tire):
    data = {'tire_pressure': 32, 'tire_tread_depth': 8}
    issues = tire.diagnose(data)
    assert not issues 
