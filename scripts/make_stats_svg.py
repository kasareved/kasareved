import json

with open("data/contributions.json") as f:
    days = json.load(f)["days"]

def n(d):
    return d.get("count", 1 if d["level"] > 0 else 0)

total = sum(n(d) for d in days)

longest = run = 0
for d in days:
    run = run + 1 if n(d) > 0 else 0
    longest = max(longest, run)

current = 0
for d in reversed(days):
    if n(d) > 0:
        current += 1
    elif d is days[-1]:
        continue          # today may not be counted yet
    else:
        break

best = max(days, key=n)

stats = [
    (f"{total:,}", "contributions"),
    (str(current), "current streak (days)"),
    (str(longest), "longest streak (days)"),
    (str(n(best)), f"best day ({best['date']})"),
]

W, H = 860, 110
tiles = ""
for i, (big, small) in enumerate(stats):
    x = i * 220
    delay = round(0.3 + i * 0.25, 2)
    tiles += (
        f'<g class="t" style="animation-delay:{delay}s">'
        f'<rect x="{x}" y="0" width="200" height="{H}" rx="8" fill="#161b22"/>'
        f'<text x="{x + 100}" y="55" class="b" text-anchor="middle">{big}</text>'
        f'<text x="{x + 100}" y="84" class="s" text-anchor="middle">{small}</text>'
        f'</g>\n'
    )

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
.b {{ font: bold 30px monospace; fill: #39d353; }}
.s {{ font: 12px monospace; fill: #8b949e; }}
.t {{ opacity: 0; animation: in 0.5s ease-out forwards; }}
@keyframes in {{ from {{ opacity: 0; transform: translateY(6px); }} to {{ opacity: 1; transform: translateY(0); }} }}
</style>
{tiles}</svg>"""

with open("stats-card.svg", "w", encoding="utf-8") as f:
    f.write(svg)
print("Wrote stats-card.svg")
