import pytest
from tools.web_search import web_search

def test_web_search_returns_answer():
    query = "What is LangChain?"
    result = web_search(query)
    
    assert "Answer:" in result
    assert "Top Sources:" in result
