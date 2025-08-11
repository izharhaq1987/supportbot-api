import os
from langchain_community.chat_models import ChatOpenAI

# inside your __init__ method
self.llm = ChatOpenAI(
    model = "gpt-4",
    temperature = 0.3,
    verbose = True,
    openai_api_key = os.getenv("OPENAI_API_KEY")
)
