import os


def load_system_prompt(prompt_name: str) -> str:
    file_path = os.path.join(os.path.dirname(__file__), f"{prompt_name}.md")

    with open(file_path, encoding="utf-8") as f:
        return f.read()
