#  SupportBot API — FastAPI + LangChain

SupportBot is a lightweight, container-ready API service that handles customer support queries. 
It can run in two modes:

- **Mock Mode** — Returns predefined, realistic responses for common support questions. Ideal for local testing, demos, and development without API costs.
- **GPT-4 Mode** — Uses OpenAI’s GPT-4 via LangChain to generate live, context-aware responses.

The service is written in Python, adheres to modern best practices, and is structured for maintainability and production deployment.

##  Overview

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) for HTTP routing and API layer.
- **LLM Integration**: [LangChain](https://www.langchain.com/) for GPT-4 orchestration and memory handling.
- **Containerization**: Minimal `Dockerfile` with a non-root runtime user.
- **Environment Management**: `.env` file support with `python-dotenv`.
- **Zero-Secret Images**: No API keys stored in the image; runtime injection only.

##  Local Setup

### I. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate

II. Install Dependencies
pip install -r requirements.txt

Modes of Operation
Mock Mode (default)
Runs without any API key. Responses come from deterministic patterns.
uvicorn app:app --reload

GPT-4 Mode
Requires an OpenAI API key with GPT-4 access.

1. Create a .env file in the project root:
OPENAI_API_KEY=sk-your-real-key-here
2. Start the API:
uvicorn app:app --reload

Docker — Build & Run
SupportBot ships with a production-ready Dockerfile.
It supports both Mock and GPT-4 modes.

I. Build the Image
docker build -t supportbot-api:latest .

II. Run in Mock Mode
docker run --rm -p 8000:8000 supportbot-api:latest

III. Run in GPT-4 Mode
docker run --rm -p 8000:8000 \
  -e OPENAI_API_KEY=sk-your-real-key \
  supportbot-api:latest

IV. Test the Endpoint
curl -X POST http://127.0.0.1:8000/ask \
     -H "Content-Type: application/json" \
     -d '{"message":"Hi, how can I update my account information?"}'

Mock Mode example response:
{
  "reply": "(Mock) I hear you: “Hi, how can I update my account information?”. Tell me a bit more and I’ll point you to the right steps."
}

 Example Usage (Local or Docker)
curl -X POST http://127.0.0.1:8000/ask \
     -H "Content-Type: application/json" \
     -d '{"message":"How do I reset my password?"}'

Project Layout
supportbot-api/
├── app.py               # FastAPI application entry point
├── langchain_agent.py   # Core bot logic, memory, and mode switching
├── examples/
│   ├── ask_request.json # Sample API request payload
│   └── ask_curl.sh      # Simple curl test script
├── Dockerfile           # Container build file
├── .dockerignore        # Docker build exclusions
├── .gitignore           # Git exclusions
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
└── .env (optional)      # API key for GPT-4 mode

Managing Requirements
If you need to regenerate the dependency list:
pip install fastapi uvicorn langchain langchain-community python-dotenv openai
pip freeze > requirements.txt

License
MIT License — You are free to use, modify, and distribute this code, provided that the license notice is included with your copies.
