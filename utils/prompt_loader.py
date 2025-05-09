# utils/prompt_loader.py

import os

def load_prompt(prompt_name: str) -> str:
    """
    Loads a prompt template from the prompts/ directory by filename.
    Example: load_prompt("summary_prompt.txt")
    """
    base_path = os.path.dirname(os.path.dirname(__file__))
    prompt_path = os.path.join(base_path, "prompts", prompt_name)

    if not os.path.exists(prompt_path):
        raise FileNotFoundError(f"Prompt file '{prompt_name}' not found in /prompts")

    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()
