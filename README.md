# SupportBot API (FastAPI + LangChain)

A simple **customer support bot API** built with **FastAPI** and **LangChain**, designed to handle customer queries via GPT-4 or a local **Mock Mode** for development without API costs.

---

##  Project Overview

SupportBot exposes a single `/ask` endpoint. 
- **GPT-4 Mode**: Uses OpenAI’s GPT-4 via LangChain to generate real responses. 
- **Mock Mode**: Returns helpful, pre-programmed responses for common intents — no API key required. 

The project includes:
- `app.py`: FastAPI API server 
- `langchain_agent.py`: Bot logic, memory, and mode switching 
- `examples/`: Ready-to-run JSON and `cURL` examples 
- `.env` support for easy API key management 

---

##  Setup

###  Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
2.  Install dependencies
pip install -r requirements.txt
Modes of Operation
Mock Mode (default)
Runs without any API key, using deterministic mock replies.
uvicorn app:app --reload
GPT-4 Mode
Requires an OpenAI API key:

Create .env in the project root:
OPENAI_API_KEY=sk-your-real-key-here
Start the server:
uvicorn app:app --reload
 Example cURL
curl -X POST http://127.0.0.1:8000/ask \
     -H "Content-Type: application/json" \
     -d '{"message":"Hi, how can I update my account information?"}'
Mock Mode sample response:
{
  "reply": "(Mock) I hear you: “Hi, how can I update my account information?”. Tell me a bit more and I’ll point you to the right steps."
}
 Project Structure
supportbot-api/
├── app.py
├── langchain_agent.py
├── examples/
│   ├── ask_request.json
│   └── ask_curl.sh
├── README.md
├── requirements.txt
└── .gitignore
🧾 Requirements

pip install fastapi uvicorn langchain langchain-community python-dotenv openai
pip freeze > requirements.txt
 License
MIT License – feel free to use and modify for your needs.
