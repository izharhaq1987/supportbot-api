# langchain_agent.py

import os
from typing import List

from dotenv import load_dotenv

# Use community namespace to avoid deprecation warnings
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent


load_dotenv()


class SupportBotAgent:
    def __init__(self) -> None:
        self.api_key = os.getenv("OPENAI_API_KEY", "").strip()
        self.is_mock = (self.api_key == "")

        # Keep a simple memory either way; LangChain’s memory works fine without calling the LLM
        self.memory = ConversationBufferMemory(
            memory_key = "chat_history",
            return_messages = True
        )

        if self.is_mock:
            # No API key: run in mock mode
            self.tools = []
            self.agent = None
        else:
            # Real GPT-4 mode
            self.tools = []
            self.agent = initialize_agent(
                tools = self.tools,
                llm = ChatOpenAI(
                    model = "gpt-4",
                    temperature = 0.3,
                    verbose = True,
                    openai_api_key = self.api_key
                ),
                memory = self.memory,
                agent = "chat-zero-shot-react-description",
                verbose = True
            )

    def run(self, user_input: str) -> str:
        """
        Route to GPT-4 if configured; otherwise use a deterministic mock for local testing.
        """
        if self.is_mock:
            # Store into memory for parity with the real path
            self._remember(user_input)
            return self._mock_reply(user_input)

        return self.agent.run(user_input)

    # ----- Mock helpers -----

    def _remember(self, user_input: str) -> None:
        """
        Append user input to memory in a minimal way so we can simulate continuity.
        """
        # ConversationBufferMemory expects messages; we can fake a simple trace.
        # For now, we do nothing complex. This keeps mock predictable and side‑effect free.
        pass

    def _mock_reply(self, user_input: str) -> str:
        """
        Deterministic, human-readable responses to common support intents.
        Keeps output simple and useful for testing the API wrapper.
        """
        text = user_input.lower().strip()

        # Basic intent sniffing
        if "reset" in text and "password" in text:
            return (
                "No worries. To reset your password:\n"
                "I. Go to Settings → Security\n"
                "II. Click “Reset Password”\n"
                "III. Check your email for the reset link (valid for 15 minutes)\n"
                "If you don’t receive it, check spam or ask me to resend."
            )

        if ("refund" in text) or ("money back" in text):
            return (
                "I can help with refunds. Please share your order number.\n"
                "Our standard window is 30 days from delivery. "
                "Once approved, refunds post within 3–5 business days."
            )

        if ("hours" in text) or ("open" in text) or ("opening" in text):
            return "We’re available 24/7 via chat. Phone support is 9am–6pm ET, Monday–Friday."

        if ("agent" in text) or ("human" in text) or ("representative" in text):
            return (
                "I can escalate this. Please provide your email and best callback time. "
                "A specialist will reach out within one business day."
            )

        if ("email" in text and ("change" in text or "update" in text)):
            return (
                "To change your account email:\n"
                "I. Settings → Account\n"
                "II. Update Email\n"
                "III. Confirm via the verification link we send"
            )

        if ("shipping" in text) or ("track" in text) or ("order status" in text):
            return (
                "I can check that. Share your order number. "
                "If you have a tracking ID, you can also paste it here."
            )

        if ("price" in text) or ("pricing" in text) or ("cost" in text) or ("plan" in text):
            return (
                "Our plans are:\n"
                "I. Starter: $9/month\n"
                "II. Pro: $29/month\n"
                "III. Team: $79/month\n"
                "Annual billing saves 15%."
            )

        if text in {"hi", "hello", "hey"} or "help" in text:
            return (
                "Hi there! I can help with passwords, orders, billing, and account updates. "
                "What do you need today?"
            )

        # Default mock
        return f"(Mock) I hear you: “{user_input}”. Tell me a bit more and I’ll point you to the right steps."
