import json
from datetime import datetime
import markdown
from pathlib import Path
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
            title = item.get("title", "Untitled").replace('\n', ' ').strip()
            trends_content += (
                f"\n### {fire_emoji} {title}\n\n"
                f"- **Source**: {source_emoji} {item['type'].capitalize()}\n"
                f"- **Metrics**: {item['metrics']}\n"
                f"- **Link**: [{item['url'].split('//')[-1].split('/')[0]}]({item['url']})\n\n"
            )
    # prepare for markdown
    # replace dynamic content in template
    report = template.replace("{{DATE}}", report_date)
    report = report.replace("{{TRENDS}}", trends_content)
    report = report.replace("{{ITEM_COUNT}}", str(sum(len(i) for i in data["trends"].values())))

    # 
    with open('tech_trends_report.md', 'w', encoding='utf-8') as f:
        f.write(report)

    # prepare for html
    with open('templates/report_template.html', 'r', encoding='utf-8') as f:
        html_template = f.read()
        
    html_content = markdown.markdown(report)
    template_html = html_template.replace("{{DATE}}", report_date)
    template_html = template_html.replace("{{ITEM_COUNT}}", str(sum(len(i) for i in data["trends"].values())))
    template_html = template_html.replace("<!-- CONTENT_PLACEHOLDER -->", html_content)

    with open('tech_trends_report.html', 'w', encoding='utf-8') as f:
        f.write(template_html)
    
    print(f"Generated report with {len(data['trends'])} categories")


if __name__ == "__main__":
    generate_report()