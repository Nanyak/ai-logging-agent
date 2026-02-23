"""
Google Gemini model wrapper.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from ..config import Config

class GeminiModel:
    """Wrapper for Google Gemini model."""
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(
            model=Config.GENMINI_MODEL,
            google_api_key=Config.GEMINI_API_KEY,
            temperature=Config.TEMPERATURE
        )

    def get_llm(self):
        """Return the underlying language model instance."""
        return self.model

    def get_llm_with_tools(self, tools):
        """Return the language model instance with tools bound."""
        return self.model.bind_tools(tools)