# agents/main_agent.py

from langchain.agents import initialize_agent, AgentType
from langchain.agents import Tool
from langchain_groq import ChatGroq
from configs.settings import GROQ_API_KEY
from tools.web_search import web_search
from tools.page_crawler import crawl_page
from tools.summarizer import summarize_text
from tools.semantic_crawler import crawl_semantic_content

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="meta-llama/llama-4-scout-17b-16e-instruct" #"qwen-qwq-32b" #"mixtral-8x7b-32768"  # or use "llama3-70b-8192" if you want LLaMA
)

tools = [
    Tool(name="WebSearch", func=web_search, description="Search the web given a query"),
    # Tool(name="PageCrawler", func=crawl_page, description="Crawl and extract readable text from a web URL"),
    Tool(name="PageCrawler", func=crawl_semantic_content, description="Crawl and extract readable text from a web URL"),
    Tool(name="Summarizer", func=summarize_text, description="Summarize large blocks of text into concise summaries. Only use when you are asked to summarize things."),
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)





