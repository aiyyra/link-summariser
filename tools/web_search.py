from tavily import TavilyClient
from configs.settings import TAVILY_API_KEY

client = TavilyClient(api_key=TAVILY_API_KEY)

def web_search(query: str) -> str:
    """
    Perform a web search using Tavily and return relevant text results.
    """
    try:
        result = client.search(query=query, search_depth="basic", include_answer=True)
        answer = result.get("answer", "")
        sources = result.get("results", [])

        combined_sources = "\n".join(
            [f"- {s['title']}: {s['url']}" for s in sources[:3]]
        )

        return f"Answer: {answer}\n\nTop Sources:\n{combined_sources}"

    except Exception as e:
        return f"[WebSearch Error] {e}"
