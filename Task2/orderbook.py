import websockets
import json
from priorityQ import priorityQA,priorityQB
import asyncio

level=5
asks=priorityQA()
bids=priorityQB()
long_url='wss://stream.binance.com:9443/ws/bnbusdt@depth'

async def handle(message):
    '''
    handle the incoming websocket message
    
    Args:
    message: incoming websocket message
    '''
    data=json.loads(message)

    # get the data, in here we should update the priority queue
    bid=data['b']
    ask=data['a']
    for i in range(len(bid)):
        if bids.full()==True:
            bids.pop()
        bids.update(float(bid[i][0]),float(bid[i][1]))  

    for i in range(len(ask)):
        if asks.full()==True:
            data=asks.pop()
            
        asks.update(float(ask[i][0]),float(ask[i][1]))
    print(asks.queue.queue)



# def on_error(ws,error):
#     print(f"Error: ",error)

# def on_close( ws):
#     print("### closed ###")


async def websocket_connection_stream():
    '''
    websocket connection to the server
    '''
    while True:
        try:
            async with websockets.connect(long_url) as websocket:
                while True:
                    try:
                        message = await websocket.recv()
                        asyncio.create_task(handle(message))
                    except websockets.exceptions.ConnectionClosedError:
                        print("Connection closed")
                        break
        except websockets.exceptions.WebSocketException as e:
            print(f"websocket connection ,Error: {e}, retrying...")
            await asyncio.sleep(5)


def initial_snapshot( init_snapshot):
    '''
    initial snapshot of the orderbook
    
    Args: 
    init_snapshot: initial snapshot of the orderbook
    
    '''
    level=5
    for i in range(len(init_snapshot['bids'][:level])):
        bids.push(init_snapshot['bids'][i][0],init_snapshot['bids'][i][1])
        

    for i in range(len(init_snapshot['asks'][:level])):
        asks.push(init_snapshot['asks'][i][0],init_snapshot['asks'][i][1])
        

async def main():
    initial_snapshot_dict={'bids':[[1,2],[2,3],[3,4],[4,5],[5,6]],'asks':[[6,5],[7,4],[8,3],[9,2],[10,1]]}

    initial_snapshot(initial_snapshot_dict)
    await websocket_connection_stream()


asyncio.run(main())