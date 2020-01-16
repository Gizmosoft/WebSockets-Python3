# WS client example

import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        greet = input("Bot> Hello! Would you want to report any cybercrime? ") #first question, answer in YES/NO
        if(greet == "Yes"):
            await websocket.send(greet)
            print(f"User> {greet}")         #send the response

            response = await websocket.recv()       #recv response from bot
            print(f"Bot> {response}")
            list = await websocket.recv()               #recv the list of frauds. This has to be links in rt
            print(f"Bot> {list}")
            test = await websocket.recv()
            print(f"Bot> {test}")
            next_var = await websocket.recv()
            print(f"Bot> {next_var}")
            test2 = await websocket.recv()
            print(f"Bot> {test2}")
        else:
            await websocket.send(greet)
            print(f"User> {greet}")             #send the response
            goodbye = await websocket.recv()    #recv the goodbye message
            print(f"Bot> {goodbye}")

        # greeting = await websocket.recv()
        # print(f"< {greeting}")

while True:
    asyncio.get_event_loop().run_until_complete(hello())
# asyncio.get_event_loop().run_forever()
