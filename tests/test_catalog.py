import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_catalog_has_at_least_30_projects():
 data=json.loads((ROOT/'data'/'project_catalog.json').read_text()); assert len(data)>=30
def test_catalog_entries_have_fields():
 data=json.loads((ROOT/'data'/'project_catalog.json').read_text());
 for item in data: assert item['title'] and item['category'] and item['description']
