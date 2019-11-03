import asyncio
import json
import logging
import websockets

logging.basicConfig()

USERS = set()


async def register(websocket):
    USERS.add(websocket)
    # await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)


async def deploy_service(websocket, path):
    await register(websocket)
    try:
        # await websocket.send()
        async for message in websocket:
            data = json.loads(message)
            print(data)
            await websocket.send('data received')

    finally:
        await unregister(websocket)


start_server = websockets.serve(deploy_service, '0.0.0.0', 6789)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()