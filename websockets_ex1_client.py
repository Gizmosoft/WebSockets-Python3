# WS client example

import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("Hello! How may I help you? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

while(1):
    asyncio.get_event_loop().run_until_complete(hello())
# asyncio.get_event_loop().run_forever()
