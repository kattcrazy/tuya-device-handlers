"""Quirk for Contact sensor (product_id p6sqiuesvhmhvv4f).

Tuya does not advertise any datapoints for this device.
"""

from tuya_device_handlers import TUYA_QUIRKS_REGISTRY
from tuya_device_handlers.builder import DeviceQuirk
from tuya_device_handlers.const import DPMode

(
    DeviceQuirk()
    .applies_to(product_id="p6sqiuesvhmhvv4f")
    .add_dpid_boolean(
        dpid=1,
        dpcode="doorcontact_state",
        dpmode=DPMode.READ,
    )
    .add_dpid_enum(
        dpid=102,
        dpcode="battery_state",
        dpmode=DPMode.READ,
        enum_range=["low", "middle", "high"],
    )
    .set_dpid_strategy_to_enum(
        dpid=1,
        dpcode="doorcontact_state",
        enum_mapping_map={"some_true_value": True, "some_false_value": False},
    )
    .register(TUYA_QUIRKS_REGISTRY)
)
