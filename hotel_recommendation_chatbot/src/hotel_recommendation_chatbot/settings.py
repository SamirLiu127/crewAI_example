import os
from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

LLM_SETTINGS = {
    "openai": {
        "model": "gpt-4o-mini",
        "api_key": os.getenv('OPENAI_API_KEY')
    },
    "ollama": {
        "model": "llama3.1:8b", 
        "base_url": os.getenv('OLLAMA_BASE_URL')
    },
    "anthropic": {
        "model": "claude-3-7-sonnet-20250219",
        "api_key": os.getenv('ANTHROPIC_API_KEY')
    }
}

LLM_SETTINGS = LLM_SETTINGS["openai"] # Change this to switch between LLMs

llm = LLM(
    model=LLM_SETTINGS["model"],
    api_key=LLM_SETTINGS["api_key"]
)