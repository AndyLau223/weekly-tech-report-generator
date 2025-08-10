import requests
import json
import os
from datetime import datetime, timedelta
import feedparser


class SourceCollector:
    def __init__(self, config_path="config/sources.json"):
        with open(config_path, "r") as f:
            self.sources = json.load(f)
        self.results = {}
        self.fetchers = {
            "github": self.fetch_github_trading,
            "arxiv": self.fetch_arxiv_papers,
            "stackoverflow": self.fetch_stackoverflow_questions,
            "huggingface": self.fetch_huggingface_trends
        }

    def fetch_huggingface_trends(self):
        url = "https://huggingface.co/api/models"
        params = {"sort": "downloads", "direction": -1, "limit": 20}
        response = requests.get(url, params=params)
        response.raise_for_status()

        models = response.json()

        return [
            {
                "title": model["modelId"],
                "url": f"https://huggingface.co/{model['modelId']}",
                "downloads": model.get("downloads", 0),
                "tags": model.get("tags", []),
                "type": "huggingface",
            }
            for model in models
            if model.get("downloads", 0)
            > self.sources["ai"]["huggingface"]["min_downloads"]
        ]

    def fetch_github_trading(self):
        url = "https://api.github.com/search/repositories"
        params = {
            "q": f"created:>{(datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')}",
            "sort": "stars",
            "order": "desc",
            "per_page": 20,
        }
        headers = {"Accept": "application/vnd.github.v3+json"}
        token = os.environ.get("GITHUB_TOKEN")
        if token:
            headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return [
            {
                "title": item["name"],
                "url": item["html_url"],
                "stars": item["stargazers_count"],
                "description": item["description"] or "",
            }
            for item in response.json().get("items", [])
        ]

    def fetch_arxiv_papers(self):
        url = "http://export.arxiv.org/api/query"
        params = {
            "search_query": "cat:cs.*",
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "max_results": 15,
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        feed = feedparser.parse(response.text)
        return [
            {
                "title": entry.title,
                "url": entry.id,
                "summary": entry.summary,
                "published": entry.published,
            }
            for entry in feed.entries
        ]

    def fetch_stackoverflow_questions(self):
        url = "https://api.stackexchange.com/2.3/questions"
        params = {
            "order": "desc",
            "sort": "activity",
            "site": "stackoverflow",
            "filter": "withbody",
            "pagesize": 5,
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return [
            {
                "title": item["title"],
                "url": item["link"],
                "summary": item["body"],
                "published": item["creation_date"],
            }
            for item in data.get("items", [])
        ]

    def collect(self):
        for source in self.sources.get("enabled", []):
            print(f"Fetching {source}...")
            fetcher = self.fetchers.get(source)
            if fetcher:
                try:
                    self.results[source] = fetcher()
                except Exception as e:
                    print(f"Error fetching {source}: {e}")

    def save(self, output_path="raw_data.json"):
        with open(output_path, "w") as f:
            json.dump(self.results, f, indent=2)
        print(
            f"Collected {sum(len(v) for v in self.results.values())} items from {len(self.results)} sources."
        )


def main():
    collector = SourceCollector()
    collector.collect()
    collector.save()


if __name__ == "__main__":
    main()
