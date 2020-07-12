# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets

#prints time and date continuosly
async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

async def welcome(websocket, path):
    WELCOME_INTENT = ["Hello! I am CyberEye. How may I help you?\n",
                      "Hi! I am CyberEye. How may I help you?\n",
                      "Hey! I am CyberEye. How may I help you?\n"]
    wel = random.choice(WELCOME_INTENT)
    await websocket.send(wel)
    return next_method()

async def next_method(websocket):
    next = "Here we are in next function!"
    await websocket.send(next)

start_server = websockets.serve(welcome, "127.0.0.1", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
