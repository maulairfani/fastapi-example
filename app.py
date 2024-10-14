from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

def generate_stream():
    for i in range(10):
        yield f"Chunk {i+1}\n"
        time.sleep(1)  # Simulasi delay 1 detik per chunk

@app.get("/stream")
def stream_response():
    return StreamingResponse(generate_stream(), media_type="text/plain")
