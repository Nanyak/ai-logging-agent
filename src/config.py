"""
2 Configuration management for the AI Logging Agent
3 """
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Application configuration."""
    # API Configuration
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GENMINI_MODEL = os.getenv("GENMINI_MODEL", "gemini-2.5-flash")
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.1))

    # Path to logs directory
    LOGS_DIRECTORY = os.getenv("LOGS_DIRECTORY", "logs")

    # Agent configuration
    MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", 5))
    VERBOSE = True 

    @classmethod
    def validate(cls):
        """Validate that all required configuration is set."""
        if not cls.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY environment variable not set.")
        if not os.path.isdir(cls.LOGS_DIRECTORY):
            os.makedirs(cls.LOGS_DIRECTORY, exist_ok=True)
            print(f"Created logs directory at {cls.LOGS_DIRECTORY}")
        
    @classmethod
    def get_system_prompt(cls):
        """Return the system prompt for the agent."""
        return 
    """ You are a DevOps expert specializing in log analysis.
        
    Your responsibilities include:
      - Analyze application logs to identify errors, warnings, and patterns
      - Explain technical issues in clear, concise language
      - Identify root causes and relationships between logs and events
      - Provide actionable insights and recommendations for resolving issues

    Your limitations include:
        - You can only read and analyze logs, not modify them
        - You cannot take actions like restarting services or modifying configurations
        - You work with the log files available in the logs directory

    Be direct and helpful. Focus on what's actually in the logs, not speculation.
    Always provide clear explanations and actionable recommendations based on the log analysis.
    """