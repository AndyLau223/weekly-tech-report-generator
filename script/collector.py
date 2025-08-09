import requests
import json
import os
from datetime import datetime, timedelta

# 加载数据源配置
with open('../config/sources.json') as f:
    SOURCES = json.load(f)

def fetch_github_trending():
    """获取GitHub趋势项目"""
    url = "https://api.github.com/search/repositories"
    params = {
        "q": "created:>" + (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d"),
        "sort": "stars",
        "order": "desc",
        "per_page": 20
    }
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, params=params, headers=headers)
    return [{
        "title": item["name"],
        "url": item["html_url"],
        "stars": item["stargazers_count"],
        "description": item["description"]
    } for item in response.json()["items"]]

def fetch_arxiv_papers():
    """获取arXiv最新论文"""
    url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": "cat:cs.*",
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": 15
    }
    response = requests.get(url, params=params)
    # 解析XML响应（简化版）
    return [{
        "title": entry.title.text,
        "url": entry.id.text,
        "summary": entry.summary.text[:200] + "..."
    } for entry in response.feed.entry]

def main():
    results = {}
    
    if "github" in SOURCES["enabled"]:
        results["github"] = fetch_github_trending()
    
    if "arxiv" in SOURCES["enabled"]:
        results["arxiv"] = fetch_arxiv_papers()
    
    # 保存原始数据
    with open('raw_data.json', 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()