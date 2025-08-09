import json
from datetime import datetime
import os

def generate_report():
    with open('processed_data.json') as f:
        data = json.load(f)
    
    timestamp = datetime.fromisoformat(data["timestamp"])
    report_date = timestamp.strftime("%Y-%m-%d")
    
    # 加载模板
    with open('templates/report_template.md', encoding='utf-8') as f:
        template = f.read()
    
    # 生成趋势内容
    trends_content = ""
    for category, items in data["trends"].items():
        if not items:
            continue
            
        trends_content += f"\n## {category} 领域\n"
        for item in items:
            fire_emoji = "🔥" * item["score"]
            source_emoji = {
                "github": "🐙",
                "stackoverflow": "❓",
                "arxiv": "📜"
            }.get(item["type"], "🔗")
            
            trends_content += (
                f"### {fire_emoji} {item['title']}\n"
                f"- **来源**: {source_emoji} {item['type'].capitalize()}\n"
                f"- **指标**: {item['metrics']}\n"
                f"- **链接**: [{item['url'].split('//')[-1].split('/')[0]}]({item['url']})\n\n"
            )
    
    # 插入动态内容
    report = template.replace("{{DATE}}", report_date)
    report = report.replace("{{TRENDS}}", trends_content)
    report = report.replace("{{ITEM_COUNT}}", str(sum(len(i) for i in data["trends"].values())))
    
    # 保存报告
    with open('tech_trends_report.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"Generated report with {len(data['trends'])} categories")

if __name__ == "__main__":
    generate_report()