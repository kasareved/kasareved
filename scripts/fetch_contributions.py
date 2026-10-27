import json
import requests
from bs4 import BeautifulSoup

USERNAME = "kasareved"
URL = f"https://github.com/users/{USERNAME}/contributions"

html = requests.get(URL, timeout=30).text
soup = BeautifulSoup(html, "html.parser")

days = []
for cell in soup.select("td.ContributionCalendar-day"):
    date = cell.get("data-date")
    level = int(cell.get("data-level", 0))
    if date:
        days.append({"date": date, "level": level})

days.sort(key=lambda d: d["date"])

with open("data/contributions.json", "w") as f:
    json.dump({"username": USERNAME, "days": days}, f, indent=2)

print(f"Saved {len(days)} days")
