import logging
from app.models import Device
from app.schemas import DeviceCreate, DeviceUpdate


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


async def create_device(device: DeviceCreate) -> Device:
    logger.info("Creating a new device")
    try:
        device_obj = Device.create(**device.dict())
        logger.info(f"Device created with ID: {device_obj.id}")
        return device_obj
    except Exception as e:
        logger.error(f"Error while creating device: {e}", exc_info=True)
        raise


async def get_devices(skip: int = 0, limit: int = 10) -> list[Device]:
    logger.info(f"Fetching devices with skip={skip}, limit={limit}")
    try:
        devices = list(Device.select().offset(skip).limit(limit))
        logger.info(f"Fetched {len(devices)} devices")
        return devices
    except Exception as e:
        logger.error(f"Error while fetching devices: {e}", exc_info=True)
        raise


async def get_device(device_id: int) -> Device:
    logger.info(f"Fetching device with ID: {device_id}")
    try:
        device = Device.get_or_none(Device.id == device_id)
        if device:
            logger.info(f"Device found with ID: {device_id}")
        else:
            logger.warning(f"No device found with ID: {device_id}")
        return device
    except Exception as e:
        logger.error(f"Error while fetching device: {e}", exc_info=True)
        raise


async def update_device(device_id: int, device: DeviceUpdate) -> Device:
    logger.info(f"Updating device with ID: {device_id}")
    try:
        device_obj = Device.get_or_none(Device.id == device_id)
        if device_obj:
            updates = device.dict(exclude_unset=True)
            for attr, value in updates.items():
                setattr(device_obj, attr, value)
            device_obj.save()
            logger.info(f"Device updated with ID: {device_obj.id}")
            return device_obj
        else:
            logger.warning(f"No device found with ID: {device_id}")
            return None
    except Exception as e:
        logger.error(f"Error while updating device: {e}", exc_info=True)
        raise


async def delete_device(device_id: int) -> bool:
    logger.info(f"Deleting device with ID: {device_id}")
    try:
        device = Device.get_or_none(Device.id == device_id)
        if device:
            device.delete_instance()
            logger.info(f"Device deleted with ID: {device.id}")
            return True
        else:
            logger.warning(f"No device found with ID: {device_id}")
            return False
    except Exception as e:
        logger.error(f"Error while deleting device: {e}", exc_info=True)
        raise
