"""Quirk for T & H Sensor with external probe (product_id jc1afi7ow32okd0h).

Tuya does not advertise any datapoints for this device.
They have been retrieved from the Tuya Developer Portal.

See https://github.com/home-assistant/core/issues/163205.
"""

from tuya_device_handlers import TUYA_QUIRKS_REGISTRY
from tuya_device_handlers.builder import DeviceQuirk
from tuya_device_handlers.const import DPMode

(
    DeviceQuirk()
    .applies_to(product_id="jc1afi7ow32okd0h")
    .add_dpid_integer(
        dpid=101,
        dpcode="temp_current",
        dpmode=DPMode.READ,
        unit="℃",
        min=-200,
        max=600,
        scale=1,
        step=1,
    )
    .add_dpid_integer(
        dpid=102,
        dpcode="humidity_value",
        dpmode=DPMode.READ,
        unit="%",
        min=0,
        max=100,
        scale=0,
        step=1,
    )
    .add_dpid_enum(
        dpid=103,
        dpcode="battery_state",
        dpmode=DPMode.READ,
        enum_range=["low", "middle", "high"],
    )
    .add_dpid_integer(
        dpid=104,
        dpcode="temp_calibration",
        dpmode=DPMode.READ | DPMode.WRITE,
        unit="℃",
        min=-100,
        max=100,
        scale=1,
        step=1,
    )
    .add_dpid_integer(
        dpid=105,
        dpcode="hum_calibration",
        dpmode=DPMode.READ | DPMode.WRITE,
        unit="%",
        min=-100,
        max=100,
        scale=0,
        step=1,
    )
    .add_dpid_integer(
        dpid=106,
        dpcode="temp_current_external",
        dpmode=DPMode.READ,
        unit="℃",
        min=-400,
        max=1200,
        scale=1,
        step=1,
    )
    .add_dpid_integer(
        dpid=107,
        dpcode="temp_correction",
        dpmode=DPMode.READ | DPMode.WRITE,
        unit="℃",
        min=-100,
        max=100,
        scale=1,
        step=1,
    )
    .register(TUYA_QUIRKS_REGISTRY)
)
