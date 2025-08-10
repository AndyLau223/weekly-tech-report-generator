import json
from simhash import Simhash
from collections import defaultdict
from datetime import datetime


class TrendProcessor:
    DEFAULT_TECH_MAP = {
        "AI": ["AI", "artificial intelligence", "machine learning", "deep learning"],
        "Web": ["Web", "JavaScript", "TypeScript", "React", "Vue"],
        "Cloud": ["Cloud", "AWS", "Azure", "GCP", "Kubernetes"],
        "Quantum": ["Quantum", "Qubit", "Superposition"],
        "Rust": ["Rust", "Cargo", "Wasm"],
    }

    SOURCE_CONFIG = {
        "github": {
            "score": lambda item: min(5, max(1, item.get("stars", 0) // 500 + 1)),
            "metrics": lambda item: f"⭐ {item.get('stars', 0)}",
            "text": lambda item: f"{item.get('title', '')} {item.get('description', '')}",
        },
        "stackoverflow": {
            "score": lambda item: min(5, max(1, item.get("votes", 0) // 20 + 1)),
            "metrics": lambda item: f"👍 {item.get('votes', 0)} | 💬 {item.get('answers', 0)}",
            "text": lambda item: item.get("title", ""),
        },
        "arxiv": {
            "score": lambda item: 3,
            "metrics": lambda item: item.get("summary", ""),
            "text": lambda item: item.get("title", ""),
        },
        "huggingface": {
            "text": lambda model: model.get("title", ""),
            "url": lambda model: model.get("url", ""),
            "metrics": lambda model: f"⬇️ {model.get('downloads', 0)} downloads",
            "type": "huggingface",
            "score": lambda model: min(5, model.get("downloads", 0) // 5000),
        },
    }

    def __init__(self, tech_map=None, source_config=None):
        self.tech_map = tech_map or self.DEFAULT_TECH_MAP
        self.source_config = source_config or self.SOURCE_CONFIG

    def deduplicate(self, items, keys=("title", "description"), threshold=3):
        hashes = []
        for item in items:
            text = " ".join(str(item.get(key, "")) for key in keys)
            text = text.strip() or "empty"
            hashes.append(Simhash(text))
        unique_items = []
        seen_hashes = set()
        for i, h in enumerate(hashes):
            if not any(h.distance(Simhash(seen)) < threshold for seen in seen_hashes):
                unique_items.append(items[i])
                seen_hashes.add(h.value)
        return unique_items

    def categorize(self, text):
        for category, keywords in self.tech_map.items():
            if any(kw.lower() in text.lower() for kw in keywords):
                return category
        return "Other"

    def process_source(self, items, source_type):
        config = self.source_config.get(source_type)
        if not config:
            return []
        processed = []
        for item in items:
            text = config["text"](item)
            category = self.categorize(text)
            processed.append(
                {
                    "title": item.get("title", ""),
                    "url": item.get("url", ""),
                    "score": config["score"](item),
                    "type": source_type,
                    "metrics": config["metrics"](item),
                    "category": category,
                }
            )
        return processed

    def process(self, data):
        trends = defaultdict(list)
        for source_type in self.source_config:
            items = data.get(source_type, [])
            for trend in self.process_source(items, source_type):
                category = trend.get("category") or self.categorize(trend["title"])
                trends[category].append(trend)
        # 排序并限制每类最多5个
        for category in trends:
            trends[category] = sorted(
                trends[category], key=lambda x: x["score"], reverse=True
            )[:5]
        return trends

    def run(self, raw_path="raw_data.json", output_path="processed_data.json"):
        with open(raw_path) as f:
            data = json.load(f)
        # 可配置去重源
        for key in ["github", "stackoverflow"]:
            if key in data:
                data[key] = self.deduplicate(data[key])
        trends = self.process(data)
        with open(output_path, "w") as f:
            json.dump(
                {"trends": dict(trends), "timestamp": str(datetime.now())}, f, indent=2
            )
        print(f"Processed {sum(len(v) for v in trends.values())} trending items.")


if __name__ == "__main__":
    TrendProcessor().run()
