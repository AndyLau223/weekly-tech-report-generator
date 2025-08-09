import json
from datetime import datetime

def generate_report():
    """生成Markdown格式报告"""
    with open('processed_data.json') as f:
        data = json.load(f)
    
    report_date = datetime.now().strftime("%Y-%m-%d")
    report = f"# 技术热点周报 ({report_date})\n\n"
    
    for category, items in data["trends"].items():
        report += f"## {category} 领域\n"
        for item in sorted(items, key=lambda x: x["score"], reverse=True)[:3]:
            fire_emoji = "🔥" * item["score"]
            report += (
                f"- **{item['title']}** {fire_emoji}\n"
                f"  - 来源: {'GitHub' if item['type'] == 'github' else 'arXiv'}\n"
                f"  - 链接: [{item['url']}]({item['url']})\n\n"
            )
    
    # 保存报告
    with open('tech_trends_report.md', 'w') as f:
        f.write(report)

if __name__ == "__main__":
    generate_report()