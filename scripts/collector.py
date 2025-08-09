import requests
import json
import os
from datetime import datetime, timedelta
import feedparser 

with open('config/sources.json') as f:
    SOURCES = json.load(f)

def fetch_github_trending():
    url = "https://api.github.com/search/repositories"
    params = {
        "q": f"created:>{(datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')}",
        "sort": "stars",
        "order": "desc",
        "per_page": 20
    }
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    if "GITHUB_TOKEN" in os.environ:
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    
    return [{
        "title": item["name"],
        "url": item["html_url"],
        "stars": item["stargazers_count"],
        "description": item["description"] or ""
    } for item in response.json().get("items", [])]

def fetch_arxiv_papers():
    url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": "cat:cs.*",
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": 15
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    feed = feedparser.parse(response.content)
    return [{
        "title": entry.title,
        "url": entry.link,
        "summary": (entry.summary[:200] + "...") if entry.summary else ""
    } for entry in feed.entries]

def fetch_stackoverflow():
    url = "https://api.stackexchange.com/2.3/questions"
    params = {
        "order": "desc",
        "sort": "votes",
        "tagged": ";".join(SOURCES["stackoverflow"]["tags"]),
        "site": "stackoverflow",
        "pagesize": 10,
        "fromdate": int((datetime.now() - timedelta(days=7)).timestamp())
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    return [{
        "title": item["title"],
        "url": item["link"],
        "votes": item["score"],
        "answers": item["answer_count"]
    } for item in response.json().get("items", [])]

def main():
    results = {}
    
    if "github" in SOURCES["enabled"]:
        print("Fetching GitHub trends...")
        results["github"] = fetch_github_trending()
    
    if "arxiv" in SOURCES["enabled"]:
        print("Fetching arXiv papers...")
        results["arxiv"] = fetch_arxiv_papers()
    
    if "stackoverflow" in SOURCES["enabled"]:
        print("Fetching StackOverflow questions...")
        results["stackoverflow"] = fetch_stackoverflow()
    
    with open('raw_data.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"Collected {sum(len(v) for v in results.values())} items")

if __name__ == "__main__":
    main()