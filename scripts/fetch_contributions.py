import json
import re
import requests
from bs4 import BeautifulSoup

USERNAME = "kasareved"
URL = f"https://github.com/users/{USERNAME}/contributions"

html = requests.get(URL, timeout=30).text
soup = BeautifulSoup(html, "html.parser")

# The count for each day is in a tooltip like "3 contributions on ..."
counts = {}
for tip in soup.find_all("tool-tip"):
    m = re.match(r"\s*(\d+|No)\s+contribution", tip.get_text())
    if m and tip.get("for"):
        counts[tip["for"]] = 0 if m.group(1) == "No" else int(m.group(1))

days = []
for cell in soup.select("td.ContributionCalendar-day"):
    date = cell.get("data-date")
    if date:
        days.append({
            "date": date,
            "level": int(cell.get("data-level", 0)),
            "count": counts.get(cell.get("id"), 0),
        })

days.sort(key=lambda d: d["date"])

with open("data/contributions.json", "w") as f:
    json.dump({"username": USERNAME, "days": days}, f, indent=2)

print(f"Saved {len(days)} days, {sum(d['count'] for d in days)} contributions")
