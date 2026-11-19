from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import json

app = FastAPI(title="PhonicsPal Real-Time Phoneme Streamer")

@app.get("/health")
async def health_check():
    return {"status": "ok", "pipeline": "wav2vec2-mfa-v1"}

@app.websocket("/ws/audio-stream")
async def audio_stream_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            audio_chunk = await websocket.receive_bytes()
            # TODO: Pass audio_chunk to Wav2Vec2 + MFA alignment worker
            mock_alignment = {
                "target_phoneme": "/θ/",
                "confidence": 0.62,
                "needs_micro_story": True
            }
            await websocket.send_text(json.dumps(mock_alignment))
    except WebSocketDisconnect:
        print("Client disconnected from phonics stream")
