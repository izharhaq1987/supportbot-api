from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_agent import SupportBotAgent


app = FastAPI()
agent = SupportBotAgent()


class AskRequest(BaseModel):
    message: str


@app.post("/ask")
async def ask(request: AskRequest):
    try:
        response = agent.run(request.message)
        return {"reply": response}
    except Exception as error:
        raise HTTPException(
            status_code = 500,
            detail = f"Error processing message: {str(error)}"
        )
