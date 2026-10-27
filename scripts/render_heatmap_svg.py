import json
from datetime import date

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
CELL, PITCH, LEFT, TOP = 11, 14, 12, 34

with open("data/contributions.json") as f:
    data = json.load(f)
days = data["days"]

first = date.fromisoformat(days[0]["date"])
offset = (first.weekday() + 1) % 7   # GitHub weeks start on Sunday
cols = (len(days) + offset + 6) // 7

width = LEFT * 2 + cols * PITCH
height = TOP + 7 * PITCH + 40

rects = []
for i, d in enumerate(days):
    idx = i + offset
    col, row = idx // 7, idx % 7
    x, y = LEFT + col * PITCH, TOP + row * PITCH
    color = PALETTE[min(d["level"], 4)]
    delay = round((col + row) * 0.02, 2)
    rects.append(
        f'<rect class="c" x="{x}" y="{y}" width="{CELL}" height="{CELL}" '
        f'rx="2" fill="{color}" style="animation-delay:{delay}s"/>'
    )

active = sum(1 for d in days if d["level"] > 0)
ly = TOP + 7 * PITCH + 22

legend = '<text x="%d" y="%d" class="t">Less</text>' % (width - 190, ly)
for k, c in enumerate(PALETTE):
    legend += f'<rect x="{width - 160 + k * 16}" y="{ly - 10}" width="11" height="11" rx="2" fill="{c}"/>'
legend += '<text x="%d" y="%d" class="t">More</text>' % (width - 72, ly)

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<style>
.t {{ font: 11px monospace; fill: #8b949e; }}
.c {{ opacity: 0; animation: pop 0.4s ease-out forwards; }}
@keyframes pop {{ from {{ opacity: 0; transform: translateY(-6px); }} to {{ opacity: 1; transform: translateY(0); }} }}
</style>
<rect width="100%" height="100%" rx="8" fill="#0d1117"/>
<text x="{LEFT}" y="22" class="t">{active} active days in the last year</text>
{''.join(rects)}
{legend}
</svg>"""

with open("contrib-heatmap.svg", "w", encoding="utf-8") as f:
    f.write(svg)
print("Wrote contrib-heatmap.svg")
