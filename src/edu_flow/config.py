import os

LLM_CONFIGS = {
    "openai": {
        "model": "gpt-4o-mini",
        "api_key": os.getenv('OPENAI_API_KEY'),
        "base_url": "",
    },
    "groq": {
        "model": "groq/llama3-groq-70b-8192-tool-use-preview", 
        "api_key": os.getenv('GROQ_API_KEY'),
        "base_url": "",
    },
    "anthropic": {
        "model": "anthropic/claude-3-5-sonnet-20240620",
        "api_key": os.getenv('ANTHROPIC_API_KEY'),
        "base_url": "",
    },
    "deepspeed": {
        "model": "deepseek/deepseek-chat",
        "api_key": os.getenv('DEEPSPEED_API_KEY'),
        "base_url": "https://api.deepseek.com",
    },
}

LLM_CONFIG = LLM_CONFIGS["deepspeed"] # Change this to switch between LLMs

EDU_FLOW_INPUT_VARIABLES = {
    "audience_level": "intermediate",
    "topic": "Automated reasoning"
} 