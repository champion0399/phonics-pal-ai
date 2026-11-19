# PhonicsPal AI 🎙️📖

Real-time adaptive phonics learning app for kids (ages 4–7). Listens to children read aloud via WebSockets, pinpoints exact phoneme-level mispronunciations using Wav2Vec2 + Montreal Forced Aligner (MFA), and dynamically generates decodable micro-stories targeting their weak spots.

## 🏗️ Architecture & Tech Stack

- **Frontend:** React Native (Interactive gamified story canvas & audio capture)
- **Backend:** Python FastAPI + Async WebSockets + Redis session state
- **Speech-to-Phoneme Pipeline:** Fine-tuned `Wav2Vec2-XLSR` + `MFA` forced alignment (<200ms target latency)
- **Story Engine:** Structured LLM generation with strict phonetic-density & age-appropriate guardrails

## 🤖 Human vs. Devin Workflow

### Delegated to Devin Bots
- [x] FastAPI + WebSocket async audio-streaming boilerplate & Redis state management
- [ ] Wav2Vec2 / MFA alignment inference wrapper & sub-200ms latency benchmarks
- [ ] Synthetic kid-mispronunciation test datasets & automated `pytest` guardrails

### Human-Led
- [ ] React Native UI/UX animations & child-friendly feedback loops
- [ ] Phonics progression curriculum rules & real-audio confidence threshold tuning

## 🚀 Quick Start (Backend)

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
