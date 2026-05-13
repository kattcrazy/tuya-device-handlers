"""Test device-level quirk initialisation."""

from tests import create_device
from tuya_device_handlers.definition.binary_sensor import (
    get_default_definition as get_binary_sensor_definition,
)
from tuya_device_handlers.definition.sensor import (
    get_default_definition as get_sensor_definition,
)
from tuya_device_handlers.registry import QuirksRegistry


def test_default_definition(
    filled_quirks_registry: QuirksRegistry,
) -> None:
    """Test quirk adds missing datapoints."""
    device = create_device("tdq_p6sqiuesvhmhvv4f.json")
    assert get_binary_sensor_definition(device, "doorcontact_state") is None
    assert get_sensor_definition(device, "battery_state") is None

    filled_quirks_registry.initialise_device_quirk(device)

    assert get_binary_sensor_definition(device, "doorcontact_state") is not None
    assert get_sensor_definition(device, "battery_state") is not None
