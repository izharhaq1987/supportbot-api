# SupportBot API — FastAPI + LangChain

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Build Status](https://github.com/izharhaq1987/supportbot-api/actions/workflows/ci.yml/badge.svg)](https://github.com/izharhaq1987/supportbot-api/actions/workflows/ci.yml)
[![Docker Pulls](https://img.shields.io/docker/pulls/izharhaq86/supportbot-api.svg)](https://hub.docker.com/r/izharhaq86/supportbot-api)

SupportBot is a FastAPI-based microservice that handles customer queries using either:
- GPT-4 via OpenAI (if `OPENAI_API_KEY` is set)
- Or a deterministic mock mode for local testing and demo purposes

LangChain is used to route prompts, manage memory, and control GPT behavior. Uvicorn serves the app. The image is Docker-ready, CI-tested, and works in both local and containerized environments.

---

##  Quick Start (Local)

### I. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate

II. Install requirements
pip install -r requirements.txt

III. Run the server
uvicorn app:app --reload
Modes of Operation
Mock Mode (default)
Runs without any API key and returns realistic, hardcoded responses.
GPT-4 Mode
To enable GPT-4 replies, provide your OpenAI key:
export OPENAI_API_KEY=sk-...your-key
uvicorn app:app --reload
The agent auto-detects presence of the key and switches modes accordingly.
Docker (Pull & Run)
Skip the build process entirely and just pull the published container.

I. Pull the image
docker pull izharhaq86/supportbot-api:v0.1.0

II. Run (default: Mock Mode)
docker run --rm -p 8000:8000 izharhaq86/supportbot-api:v0.1.0

III. Run in GPT-4 Mode
docker run --rm -p 8000:8000 \
  -e OPENAI_API_KEY=sk-your-key \
  izharhaq86/supportbot-api:v0.1.0

IV. Test it
curl -X POST http://127.0.0.1:8000/ask \
     -H "Content-Type: application/json" \
     -d '{"message":"How do I reset my password?"}'

API Endpoints
| Method | Route      | Description                         |
| ------ | ---------- | ----------------------------------- |
| GET    | `/`        | Basic service check (returns JSON)  |
| GET    | `/healthz` | Health probe for CI / orchestration |
| POST   | `/ask`     | Main endpoint for support questions |

Project Structure
supportbot-api/
├── app.py                 # FastAPI entrypoint
├── langchain_agent.py     # Core agent logic (mock + GPT-4)
├── Dockerfile             # Container build
├── .dockerignore
├── requirements.txt
├── README.md
└── examples/
    ├── ask_request.json
    └── ask_curl.sh

Regenerate Requirements (Optional)
pip install -r requirements.txt
pip freeze > requirements.txt

License
MIT License — see LICENSE file for full terms.
