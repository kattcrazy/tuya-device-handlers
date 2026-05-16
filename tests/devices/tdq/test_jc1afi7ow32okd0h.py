"""Test device-level quirk initialisation."""

from tests import create_device
from tuya_device_handlers.definition.number import get_default_definition
from tuya_device_handlers.definition.sensor import get_default_definition as get_sensor
from tuya_device_handlers.registry import QuirksRegistry


def test_sensor_device_class_override_tdq(
    filled_quirks_registry: QuirksRegistry,
) -> None:
    """TDQ quirk registers explicit sensor and number device classes."""
    device = create_device("tdq_jc1afi7ow32okd0h.json")
    sensor_dpcodes = (
        "temp_current",
        "humidity_value",
        "battery_state",
        "temp_current_external",
    )
    number_dpcodes = (
        "temp_calibration",
        "hum_calibration",
        "temp_correction",
    )

    for dpcode in sensor_dpcodes:
        assert get_sensor(device, dpcode) is None
    for dpcode in number_dpcodes:
        assert get_default_definition(device, dpcode) is None

    filled_quirks_registry.initialise_device_quirk(device)

    for dpcode in sensor_dpcodes:
        assert get_sensor(device, dpcode) is not None
    for dpcode in number_dpcodes:
        assert get_default_definition(device, dpcode) is not None
