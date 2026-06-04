from fastapi.middleware.cors import CORSMiddleware
from fastapi import WebSocket, WebSocketDisconnect
from core.stream_llm import stream_ai
from fastapi import FastAPI
from core.local_llm import askai
import asyncio
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "JarvisOS Running"}

@app.get("/chat")
def chat(q: str):

    response = askai(q)

    return {
        "user": q,
        "ai": response
    }
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    stop_flag = {"stop": False}

    async def receive_messages():
        """Listens for STOP signal in background"""
        nonlocal stop_flag
        try:
            while True:
                msg = await websocket.receive_text()
                if msg == "__STOP__":
                    stop_flag["stop"] = True
                else:
                    # New question received, start streaming
                    stop_flag["stop"] = False
                    asyncio.create_task(stream_response(msg))
        except WebSocketDisconnect:
            pass

    async def stream_response(question):
        """Streams AI response chunks to client"""
        stop_flag["stop"] = False
        async for chunk in stream_ai(question, stop_flag):
            if stop_flag.get("stop"):
                break
            await websocket.send_text(chunk)

    try:
        # Start listener — it handles everything
        await receive_messages()
    except WebSocketDisconnect:
        print("Client disconnected")