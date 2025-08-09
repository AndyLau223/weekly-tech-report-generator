import json
from simhash import Simhash
from collections import defaultdict

def deduplicate(items, key="title", threshold=3):
    """使用SimHash进行去重"""
    hashes = []
    for item in items:
        text = item[key] + (item.get("description", "") or "")
        hashes.append(Simhash(text))
    
    unique_items = []
    for i, current in enumerate(hashes):
        if not any(current.distance(other) < threshold for j, other in enumerate(hashes) if i != j):
            unique_items.append(items[i])
    
    return unique_items

def calculate_trend_score(item, base_stars=100):
    """计算趋势分数"""
    stars = item.get("stars", 0)
    return min(5, max(1, int(stars / base_stars) + 1))

def analyze_trends(data):
    """分析技术趋势"""
    trends = defaultdict(list)
    
    # GitHub项目分析
    for project in data.get("github", []):
        tech_keywords = ["AI", "ML", "Blockchain", "Web3", "Quantum", "Rust"]
        for keyword in tech_keywords:
            if keyword in project["title"] or keyword in project["description"]:
                trends[keyword].append({
                    "title": project["title"],
                    "url": project["url"],
                    "score": calculate_trend_score(project),
                    "type": "github"
                })
    
    # 保存处理结果
    with open('processed_data.json', 'w') as f:
        json.dump({"trends": dict(trends)}, f, indent=2)

if __name__ == "__main__":
    with open('raw_data.json') as f:
        data = json.load(f)
    
    # 数据去重
    if "github" in data:
        data["github"] = deduplicate(data["github"])
    
    analyze_trends(data)