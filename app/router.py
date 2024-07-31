from aiohttp import web
from app import crud
from app.schemas import DeviceCreate, DeviceUpdate, DeviceResponse


routes = web.RouteTableDef()


@routes.post("/devices/")
async def create_device(request: web.Request) -> web.Response:
    data = await request.json()
    device_data = DeviceCreate(**data)
    device = await crud.create_device(device_data)
    response_data = DeviceResponse.from_orm(device).dict()
    return web.json_response(response_data, status=201)


@routes.get("/devices/")
async def get_devices(request: web.Request) -> web.Response:
    skip = int(request.query.get("skip", 0))
    limit = int(request.query.get("limit", 10))
    devices = await crud.get_devices(skip=skip, limit=limit)
    response_data = [
        DeviceResponse.from_orm(device).dict()
        for device in devices
    ]
    return web.json_response(response_data)


@routes.get("/devices/{id}/")
async def get_device(request: web.Request) -> web.Response:
    device_id = int(request.match_info["id"])
    device = await crud.get_device(device_id)
    if device:
        response_data = DeviceResponse.from_orm(device).dict()
        return web.json_response(response_data)
    return web.json_response({"error": "Device not found"}, status=404)


@routes.put("/devices/{id}/")
async def update_device(request: web.Request) -> web.Response:
    device_id = int(request.match_info["id"])
    data = await request.json()
    device_data = DeviceUpdate(**data)
    device = await crud.update_device(device_id, device_data)
    if device:
        response_data = DeviceResponse.from_orm(device).dict()
        return web.json_response(response_data)
    return web.json_response({"error": "Device not found"}, status=404)


@routes.delete("/devices/{id}/")
async def delete_device(request: web.Request) -> web.Response:
    device_id = int(request.match_info["id"])
    if await crud.delete_device(device_id):
        return web.json_response({"message": "Device deleted"})
    return web.json_response({"error": "Device not found"}, status=404)
