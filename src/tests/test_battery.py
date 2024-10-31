import pytest
from components.battery import Battery


@pytest.fixture
def battery():
    return Battery()


def test_low_voltage(battery):
    data = {'battery_voltage': 11.5, 'battery_health': 80}
    issues = battery.diagnose(data)
    assert "Battery voltage is low (11.5 V)" in issues


def test_low_health(battery):
    data = {'battery_voltage': 12.5, 'battery_health': 50}
    issues = battery.diagnose(data)
    assert "Battery health is poor (50%)" in issues


def test_normal_conditions(battery):
    data = {'battery_voltage': 12.5, 'battery_health': 90}
    issues = battery.diagnose(data)
    assert not issues
