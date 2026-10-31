
import json
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

URL = "https://dblp.org/pid/44/3105.xml"

request = urllib.request.Request(
    URL,
    headers={"User-Agent": "Academic-GitHub-Pages/1.0"}
)

with urllib.request.urlopen(request, timeout=60) as response:
    root = ET.fromstring(response.read())

def get(node, tag):
    el = node.find(tag)
    return "".join(el.itertext()).strip() if el is not None else ""

records = []

for entry in root.findall("r"):
    item = next(iter(entry), None)
    if item is None:
        continue

    authors = [
        "".join(a.itertext()).strip()
        for a in item.findall("author")
    ]

    if not authors:
        authors = [
            "".join(a.itertext()).strip()
            for a in item.findall("editor")
        ]

    records.append({
        "year": get(item, "year"),
        "title": get(item, "title"),
        "authors": authors,
        "venue": get(item, "journal") or get(item, "booktitle"),
        "volume": get(item, "volume"),
        "number": get(item, "number"),
        "pages": get(item, "pages"),
        "url": get(item, "ee") or get(item, "url")
    })

records.sort(
    key=lambda p: int(p["year"]) if p["year"].isdigit() else 0,
    reverse=True
)

Path("publications.json").write_text(
    json.dumps(records, ensure_ascii=False, indent=2),
    encoding="utf-8"
)

print(f"Downloaded {len(records)} publications")
