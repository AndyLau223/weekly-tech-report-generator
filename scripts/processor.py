import json
from simhash import Simhash
from collections import defaultdict
from datetime import datetime

def deduplicate(items, keys=["title", "description"], threshold=3):
    """修复去重逻辑错误"""
    hashes = []
    for item in items:
        text = " ".join(str(item.get(key, "")) for key in keys)
        if not text.strip(): 
            text = "empty"
        hashes.append(Simhash(text))
    
    unique_items = []
    seen_hashes = set()
    
    for i, h in enumerate(hashes):
        is_duplicate = False
        for seen in seen_hashes:
            if h.distance(Simhash(seen)) < threshold:
                is_duplicate = True
                break
        
        if not is_duplicate:
            unique_items.append(items[i])
            seen_hashes.add(h.value)
    
    return unique_items

def calculate_trend_score(item):
    """统一趋势评分逻辑"""
    if "stars" in item:  # GitHub
        return min(5, max(1, item["stars"] // 500 + 1))
    elif "votes" in item:  # StackOverflow
        return min(5, max(1, item["votes"] // 20 + 1))
    else:  # arXiv论文
        return 3  # 默认值

def analyze_trends(data):
    trends = defaultdict(list)
    
    # 配置技术关键词
    tech_map = {
        "AI": ["AI", "artificial intelligence", "machine learning", "deep learning"],
        "Web": ["Web", "JavaScript", "TypeScript", "React", "Vue"],
        "Cloud": ["Cloud", "AWS", "Azure", "GCP", "Kubernetes"],
        "Quantum": ["Quantum", "Qubit", "Superposition"],
        "Rust": ["Rust", "Cargo", "Wasm"]
    }
    
    # 分析GitHub项目
    for project in data.get("github", []):
        for category, keywords in tech_map.items():
            if any(kw.lower() in (project.get("title", "") + project.get("description", "")).lower() 
                   for kw in keywords):
                trends[category].append({
                    "title": project["title"],
                    "url": project["url"],
                    "score": calculate_trend_score(project),
                    "type": "github",
                    "metrics": f"⭐ {project['stars']}"
                })
    
    # 分析StackOverflow问题
    for question in data.get("stackoverflow", []):
        for category, keywords in tech_map.items():
            if any(kw.lower() in question["title"].lower() for kw in keywords):
                trends[category].append({
                    "title": question["title"],
                    "url": question["url"],
                    "score": calculate_trend_score(question),
                    "type": "stackoverflow",
                    "metrics": f"👍 {question['votes']} | 💬 {question['answers']}"
                })
    
    # 分析arXiv论文
    for paper in data.get("arxiv", []):
        for category, keywords in tech_map.items():
            if any(kw.lower() in paper["title"].lower() for kw in keywords):
                trends[category].append({
                    "title": paper["title"],
                    "url": paper["url"],
                    "score": 3,  # 论文默认热度
                    "type": "arxiv",
                    "metrics": paper.get("summary", "")
                })
    
    # 排序并限制每类最多5个
    for category in trends:
        trends[category] = sorted(trends[category], key=lambda x: x["score"], reverse=True)[:5]
    
    with open('processed_data.json', 'w') as f:
        json.dump({"trends": dict(trends), "timestamp": str(datetime.now())}, f, indent=2)

if __name__ == "__main__":
    with open('raw_data.json') as f:
        data = json.load(f)
    
    # 数据去重
    for key in list(data.keys()):
        if key in ["github", "stackoverflow"]:
            data[key] = deduplicate(data[key])
    
    analyze_trends(data)