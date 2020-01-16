
# WS server example

import asyncio
import websockets

goodbye = f"You can contact me anytime you want. Thank you!!"
async def hello(websocket, path):
    greet = await websocket.recv()              #receive YES/NO from user
    print(f"Bot> Hello! Would you want to report any cybercrime?")
    print(f"User> {greet}")

    if(greet == "Yes"):
        response = f"Please select a cybercrime you want to report from the below list.\n"
        await websocket.send(response)      #send the above statement
        print(f"Bot> {response}")

        list = f"Lottery Scam\nJob Fraud\nPhishing\nMatrimony Scam\nOTP Fraud\n"
        await websocket.send(list)      #send the list
        print(f"Bot> {list}")

        #just for testing purpose####
        test = f"\nSending you to a new function"
        await websocket.send(test)
        print(f"Bot> {test}")
        await next(websocket, path)

        test2 = f"\nBack to hello Function"
        await websocket.send(test2)
        print(f"Bot> {test2}")
    else:
        await websocket.send(goodbye)
        print(f"Bot> {goodbye}")            #send goodbye msg in case of a NO
        

    # greeting = f"Hello {name}!"
    #
    # await websocket.send(greeting)
    # print(f"> {greeting}")

async def next(websocket, path):
    next_var = f"\nYou are in the new function!"
    await websocket.send(next_var)
    print(f"Bot> {next_var}")

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
