from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message received: {data}")
    except WebSocketDisconnect:
        print('close')
        
    # while True:
    #     data = await websocket.receive_text()
    #     await websocket.send_text(f"Message received: {data}")