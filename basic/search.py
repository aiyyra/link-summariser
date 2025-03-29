# from serpapi import GoogleSearch
from tavily import TavilyClient
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# # Tavily Search
# query = input("You: ") # Ask question here
# tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
# response = tavily_client.search(query)
# print(response)

# Tavily extract
url = "https://api.tavily.com/extract"
API_KEY = os.getenv("TAVILY_API_KEY")

payload = {
    "urls": "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "include_images": False,
    "extract_depth": "basic"
}
headers = {
    "Authorization": "Bearer " + API_KEY,
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
# response = client.extract(
#     urls=["https://blog.premai.io/state-of-text2sql-2024/"]
# )

# # Using SerpAPI
# params = {
#   "engine": "google",
#   "q": "Fresh Bagels",
#   "location": "Seattle-Tacoma, WA, Washington, United States",
#   "hl": "en",
#   "gl": "us",
#   "google_domain": "google.com",
#   "num": "10",
#   "start": "10",
#   "safe": "active",
#   "api_key": os.getenv("SERP_API_KEY")
# }

# search = GoogleSearch(params)
# results = search.get_dict()
# organic_results = results["organic_results"]

# print(organic_results)