from app.models import Device
from app.schemas import DeviceCreate, DeviceUpdate


async def create_device(device: DeviceCreate) -> Device:
    device_obj = Device.create(**device.dict())
    return device_obj


async def get_devices(skip: int = 0, limit: int = 10) -> list[Device]:
    return list(Device.select().offset(skip).limit(limit))


async def get_device(device_id: int) -> Device:
    return Device.get_or_none(Device.id == device_id)


async def update_device(device_id: int, device: DeviceUpdate) -> Device:
    device_obj = Device.get_or_none(Device.id == device_id)
    if device_obj:
        updates = device.dict(exclude_unset=True)
        for attr, value in updates.items():
            setattr(device_obj, attr, value)
        device_obj.save()
    return device_obj


async def delete_device(device_id: int) -> bool:
    device = Device.get_or_none(Device.id == device_id)
    if device:
        device.delete_instance()
        return True
    return False
