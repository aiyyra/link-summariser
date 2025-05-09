import re
from tools.page_crawler import crawl_page
from tools.summarizer import summarize_text
from agents.main_agent import agent

def is_url(text: str) -> bool:
    return re.match(r"^https?://", text.strip()) is not None

def is_long_text(text: str) -> bool:
    return len(text.split()) > 70

def route_input(user_input: str) -> str:
    """
    Normalize input before passing to agent (not bypassing it).
    """
    if is_url(user_input):
        user_input = f"Summarize this link: {user_input}"
    elif is_long_text(user_input):
        user_input = f"Summarize the following text:\n\n{user_input}"
    else:
        user_input = f"Solve this question as complete as possible: {user_input}"

    return agent.run(user_input)

