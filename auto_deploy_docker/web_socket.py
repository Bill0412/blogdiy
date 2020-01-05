import asyncio
import json
import logging
import websockets
import ssl
import pathlib
import sys

import ssh_login

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
            print('message: ', message)
            print('data: ', data)
            sys.stdout.flush()
            await websocket.send('data received')

            if 'blog_diy' in data:  # deploy info
                service = data['blog_diy']['deploy']['service']
                target = data['blog_diy']['deploy']['target']
                ssh_login.deploy_to(target['host'], int(target['port']),
                                    target['username'], target['password'], service['port'])

                success = {'wss_server': 'success'}
                await websocket.send(json.dumps(success))
    finally:
        await unregister(websocket)


ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
ssl_context.load_cert_chain(localhost_pem)

start_server = websockets.serve(deploy_service, 'deploy.blogdiy.net', 6789, ssl=ssl_context)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()