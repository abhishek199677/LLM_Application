import os
import requests
from dotenv import load_dotenv

load_dotenv()
SERP_API_KEY = os.getenv("SERP_API_KEY")


def search_google(query):
    url = f"https://serpapi.com/search.json?q={query}&api_key={SERP_API_KEY}"
    return requests.get(url).json().get("organic_results", [])