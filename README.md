# Weekly Tech Trends Report

## Overview

**Auto-Scan** is an automated pipeline for collecting, processing, and reporting trending technology topics from multiple sources. It uses GitHub Actions to generate a weekly report, categorizing hot projects, questions, and papers in fields like AI, Web, Cloud, Quantum, and Rust.

## Features

- **Data Collection:** Aggregates trending items from GitHub, StackOverflow, and arXiv.
- **Deduplication:** Uses Simhash to remove near-duplicate entries.
- **Trend Analysis:** Categorizes items by technology field using keyword mapping.
- **Scoring:** Assigns a heat score to each item for ranking.
- **Reporting:** Generates Markdown and HTML reports with a modern, tech-themed style.
- **Automation:** Runs weekly via GitHub Actions, supports email and issue publishing.

## Usage

1. **Data Sources:**  
   - `raw_data.json`: Raw data collected from all sources.
   - `processed_data.json`: Deduplicated and categorized data.

2. **Scripts:**  
   - `scripts/collector.py`: Collects raw data.
   - `scripts/processor.py`: Deduplicates and analyzes trends.
   - `scripts/reporter.py`: Generates Markdown and HTML reports.

3. **Templates:**  
   - `templates/report_template.md`: Markdown report template.
   - `templates/report_template.html`: HTML report template (tech-themed).

4. **Workflow:**  
   - `.github/workflows/weekly_report.yml`: GitHub Actions workflow for automation.

## How It Works

- The workflow runs on schedule (every Monday 14:00 Beijing time).
- Data is collected, deduplicated, and categorized.
- Reports are generated and published (Markdown/HTML).
- Optionally, reports can be sent via email or posted as GitHub Issues.

## Customization

- **Keywords:** Edit `tech_map` in `processor.py` to change technology categories.
- **Templates:** Modify files in `templates/` for custom report styles.
- **Workflow:** Adjust `.github/workflows/weekly_report.yml` for automation preferences.

## Requirements

- Python 3.10+
- `simhash` library (`pip install simhash`)
- GitHub repository with Actions enabled

## License

MIT License

---

**Auto-Scan** helps you stay up-to-date with the hottest trends in
