from html import escape

TITLE = "kasareved@github"
LINES = [
    ("Name",       "Vedant"),
    ("Now",        "Building hackathon projects, DSA"),
    ("Stack",      "Python, Java, MernStack , Git"),
    ("Location",   "Maharashtra, India"),
    ("Highlights", "Ascending"),
]

W, H = 490, 60 + len(LINES) * 30
rows = ""
for i, (k, v) in enumerate(LINES):
    y = 70 + i * 30
    d = round(0.4 + i * 0.35, 2)
    rows += (
        f'<text x="20" y="{y}" class="r" style="animation-delay:{d}s">'
        f'<tspan class="k">{escape(k)}:</tspan> '
        f'<tspan class="v">{escape(v)}</tspan></text>\n'
    )

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
text {{ font: 14px monospace; }}
.k {{ fill: #39d353; font-weight: bold; }}
.v {{ fill: #c9d1d9; }}
.r {{ opacity: 0; animation: in 0.5s ease-out forwards; }}
@keyframes in {{ from {{ opacity: 0; transform: translateX(-8px); }} to {{ opacity: 1; transform: translateX(0); }} }}
</style>
<rect width="100%" height="100%" rx="8" fill="#0d1117"/>
<rect width="100%" height="30" rx="8" fill="#161b22"/>
<circle cx="18" cy="15" r="5" fill="#ff5f56"/>
<circle cx="36" cy="15" r="5" fill="#ffbd2e"/>
<circle cx="54" cy="15" r="5" fill="#27c93f"/>
<text x="75" y="20" fill="#8b949e" style="font-size:12px">{escape(TITLE)}</text>
{rows}</svg>"""

with open("info-card.svg", "w", encoding="utf-8") as f:
    f.write(svg)
print("Wrote info-card.svg")
