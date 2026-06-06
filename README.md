# 🤖 JarvisOS

> **An enterprise-grade, personalized AI desktop operating system** — a continuously running 
> background intelligence that orchestrates local PC automation, semantic web research, and 
> academic document analysis through a Hybrid Edge-Cloud architecture.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?style=flat&logo=fastapi)
![Electron](https://img.shields.io/badge/Electron-Desktop-47848F?style=flat&logo=electron)
![Ollama](https://img.shields.io/badge/LLM-Llama_3_8B-black?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

---

## What makes JarvisOS different?

Unlike standard AI wrappers, JarvisOS runs a **true hybrid architecture**:

- 🖥️ **Edge (Your PC)** — LLM inference, voice transcription, and embeddings run locally on 
  your GPU/CPU. Your data never leaves your machine for compute.
- ☁️ **Cloud (DigitalOcean VPS)** — A Dockerized ChromaDB instance stores your semantic memory. 
  Switch from desktop to laptop — Jarvis still knows your context.
- ⚡ **Optimized payload** — Vector embeddings are generated locally; only compact numerical 
  matrices (~3KB) travel over the wire, not raw text.

---

## Core Features

| Module | Stack | Description |
|---|---|---|
| 🎙️ **Voice Interface** | faster-whisper, Silero VAD | Zero-latency PCM → WebSocket → transcription pipeline |
| 🧠 **Local LLM Brain** | Ollama, Llama-3 8B GGUF | 4-bit quantized inference, streams tokens via async generator |
| 🌐 **Cloud Memory** | ChromaDB, sentence-transformers | 384-dim vectors, HNSW indexing, cross-device persistence |
| 📄 **PDF Scholar** | PyMuPDF, LangChain | Local RAG — recursive chunking, ephemeral ChromaDB collection |
| 🔍 **Web Researcher** | Playwright, BeautifulSoup | Headless browser → HTML strip → LLM summarization |
| 🖱️ **PC Automation** | PyAutoGUI, subprocess | JSON tool dispatch → sandboxed safe_commands whitelist |
| 📅 **Study Planner** | APScheduler, SQLite | Background cron loop → proactive WebSocket reminders |
| 🎨 **Desktop GUI** | React, Electron, Framer Motion | Dark-mode neon HUD with physics-based audio visualizer |

---
---

## Quick Start

### Prerequisites
- Python 3.11+, Node.js 18+
- [Ollama](https://ollama.ai) installed locally
- A DigitalOcean account (for cloud memory — optional, degrades gracefully)

### 1. Clone & install backend
```bash
git clone https://github.com/YOUR_USERNAME/jarvisOS.git
cd jarvisOS/backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure environment
```bash
cp .env.example .env
# Fill in:
#   DO_CHROMA_IP=your.droplet.ip
#   DO_CHROMA_TOKEN=your_secret_token
```

### 3. Pull the LLM
```bash
ollama pull llama3
```

### 4. Start the backend
```bash
uvicorn main:app --reload --port 8000
```

### 5. Start the frontend
```bash
cd ../frontend
npm install
npm run dev       # or: npm run electron for desktop mode
```

---
---
## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│  EDGE — Your PC                                         │
│                                                         │
│  [ React + Electron GUI ]  ←→  WebSocket (ws://8000)   │
│                                                         │
│  [ FastAPI Orchestrator ]                               │
│    ├─ Intent Router                                     │
│    ├─ Embedding Generator  (all-MiniLM-L6-v2)          │
│    └─ Tool Executor        (Playwright · PyAutoGUI)     │
│                                                         │
│  [ Ollama Daemon ] ← Llama-3 8B loaded in VRAM         │
└──────────────────────────┬──────────────────────────────┘
                           │  HTTPS · Bearer Token Auth
┌──────────────────────────┴──────────────────────────────┐
│  CLOUD — DigitalOcean VPS ($5/mo Ubuntu Droplet)        │
│                                                         │
│  NGINX (TLS) → Docker Network → ChromaDB :8000         │
│                             └→ SQLite volume            │
└─────────────────────────────────────────────────────────┘
```

## Project Structure

```
jarvisOS/
├── backend/
│   ├── main.py                 # FastAPI entry point
│   ├── api/
│   │   └── ws_routes.py        # /chat WebSocket handler
│   ├── core/
│   │   ├── orchestrator.py     # Central state machine
│   │   ├── cloud_memory.py     # ChromaDB HTTP client → DigitalOcean
│   │   ├── local_llm.py        # Async Ollama streaming wrapper
│   │   └── embedding.py        # sentence-transformers generator
│   └── tools/
│       ├── pc_control.py       # PyAutoGUI + sandboxed subprocess
│       ├── web_agent.py        # Playwright headless browser
│       └── pdf_parser.py       # PyMuPDF + LangChain chunker
├── frontend/
│   ├── electron/main.js
│   └── src/
│       ├── components/
│       ├── hooks/useWebSocket.js
│       └── App.jsx
└── deployment/
    ├── Dockerfile
    └── docker-compose.yml
```

## Engineering Highlights

- **Async-first**: FastAPI + `asyncio` keeps LLM token streaming non-blocking alongside I/O tool calls
- **Semantic search**: Cosine similarity over 384-dim HNSW index — `O(log N)` retrieval, not `O(N)`
- **Resilient**: Cloud memory timeout falls back to local Redis cache with graceful degradation
- **Privacy-preserving**: Only vector matrices (not text) leave your machine for cloud memory queries
- **Production patterns**: `python-dotenv` config, structured `logging` with timestamps, strict CORS

---

## Development Roadmap

- [x] Phase 1 — FastAPI backbone
- [x] Phase 2 — Voice (Whisper + VAD)
- [x] Phase 3 — Local LLM streaming
- [x] Phase 4 — PC automation sandbox
- [x] Phase 5 — Web research agent
- [x] Phase 6 — PDF intelligence
- [x] Phase 7 — Cloud memory (DigitalOcean)
- [ ] Phase 8 — Study planner + APScheduler
- [ ] Phase 9 — React + Electron desktop UI
- [ ] Phase 10 — Full WebSocket duplex
- [ ] Phase 11 — Framer Motion UI polish
- [ ] Phase 12 — Packaging + electron-builder

---

## License

MIT © [ADITI SHARMA]
