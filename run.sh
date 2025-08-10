#!/bin/bash
source venv/bin/activate
pip install -r requirements.txt

echo "Running data collector..."
python scripts/collector.py
echo "Data collection complete."


echo "Running data processor..."
python scripts/processor.py
echo "Data processing complete."


echo "Running data reporter..."
python scripts/reporter.py
echo "Data reporting complete."
