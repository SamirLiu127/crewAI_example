import os
from crewai import LLM
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # General settings
    verbose = os.getenv('VERBOSE', False) == True
    
    # LLM provider configurations
    LLM_PROVIDERS = {
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
    
    # Default LLM provider
    active_provider = "openai"
    
    @classmethod
    def get_llm_config(cls):
        return cls.LLM_PROVIDERS[cls.active_provider]
    
    @classmethod
    def get_llm(cls):
        config = cls.get_llm_config()
        return LLM(
            model=config["model"],
            api_key=config.get("api_key"),
            base_url=config.get("base_url")
        )


# Create settings instance for backward compatibility
SETTINGS = Settings
llm = Settings.get_llm()