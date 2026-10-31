
import json
import urllib.request
from pathlib import Path

DBLP_URL = "https://dblp.org/pid/44/3105.json"

request = urllib.request.Request(
    DBLP_URL,
    headers={
        "User-Agent": "Mozilla/5.0 (compatible; AcademicWebsite/1.0)",
        "Accept": "application/json"
    }
)

with urllib.request.urlopen(request, timeout=60) as response:
    raw = response.read()
    content_type = response.headers.get("Content-Type", "")

print("Content-Type:", content_type)
print("Response preview:", raw[:200])

try:
    data = json.loads(raw)
except json.JSONDecodeError as exc:
    raise RuntimeError(
        "DBLP did not return valid JSON. "
        f"Response starts with: {raw[:200]!r}"
    ) from exc

records = []

def as_text(value):
    if value is None:
        return ""
    if isinstance(value, dict):
        return str(value.get("text", ""))
    return str(value)

for entry in data.get("result", {}).get("hits", {}).get("hit", []):
    info = entry.get("info", {})

    authors_data = info.get("authors", {}).get("author", [])
    if isinstance(authors_data, dict):
        authors_data = [authors_data]

    authors = [as_text(a) for a in authors_data]

    records.append({
        "year": as_text(info.get("year")),
        "title": as_text(info.get("title")),
        "authors": authors,
        "venue": as_text(info.get("venue")),
        "volume": as_text(info.get("volume")),
        "number": as_text(info.get("number")),
        "pages": as_text(info.get("pages")),
        "url": as_text(info.get("ee")) or as_text(info.get("url"))
    })

records.sort(
    key=lambda p: int(p["year"]) if p["year"].isdigit() else 0,
    reverse=True
)

if not records:
    raise RuntimeError(
        "No publications found. "
        "The DBLP JSON structure may differ from the expected format."
    )

Path("publications.json").write_text(
    json.dumps(records, ensure_ascii=False, indent=2),
    encoding="utf-8"
)

print(f"Successfully downloaded {len(records)} publications.")
