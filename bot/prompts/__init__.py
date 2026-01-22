import os
from datetime import datetime

def load_system_prompt(**kwargs) -> str:
    prompt_path = os.path.join(os.path.dirname(__file__), "system_prompt.md")
    
    with open(prompt_path, encoding="utf-8") as f:
        return f.read()