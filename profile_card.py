"""
Generates profile-card.svg — a neofetch-style terminal card: ASCII-art
portrait on the left, dot-leader info panel on the right. Matches the
KARTHIK1749/KARTHIK1749 reference layout exactly (same sections/order),
filled in with your own info and photo.

Usage:
    python profile_card.py photo.jpg

Requires:
    pip install pillow
"""

import sys
from PIL import Image, ImageOps

# ---------------- Your info ----------------
HANDLE = "Ali@Neural-Grid"

FIELDS_1 = {
    "Subject": "Ali Asghar",
    "Role": "AI/ML Engineer",
    "Origin": "Naushero Feroze, Pakistan",
    "Status": "Building . Learning . Shipping",
    "ToolChain": "VS Code, Git, GitHub, Postman",
}

FIELDS_2 = {
    "Neural.Core": "Python, JavaScript, TypeScript",
    "Neural.AI": "ML, Deep Learning, CV, NLP, GenAI",
    "Neural.Frontend": "React, Next.js, HTML/CSS, Tailwind",
    "Neural.Backend": "Node.js, Express, Django, Flask",
    "Neural.Stack": "MERN, Django, Flask",
}

CONTACT = {
    "Grid.Mail": "aliasghargh540@gmail.com",
    "Grid.Portfolio": "portfolio-asghar-ali.vercel.app",
    "Grid.LinkedIn": "ali-asghar-a730322bb",
    "Grid.Github": "AsgharGhanghro",
}

# GitHub Stats — fill in your real numbers (or wire a GitHub Action step
# that fetches them via the API and rewrites this dict before running).
STATS_LINE_1 = "Repos: -   Stars: -"
STATS_LINE_2 = "Commits: -   Followers: -"
STATS_LINE_3 = "Lines of Code on GitHub: -"
# --------------------------------------------

ASCII_CHARS = "@%#*+=-:. "
ART_WIDTH = 110    # characters wide — higher = more recognizable detail
FONT_ASPECT = 0.5  # monospace chars are taller than wide

LABEL_WIDTH = 16   # characters reserved for "Label:" before dot leaders
DOTS_WIDTH = 22    # how many dot-leader characters to draw


def image_to_ascii(path, width=ART_WIDTH):
    img = Image.open(path).convert("L")
    img = ImageOps.autocontrast(img, cutoff=1)
    w, h = img.size
    new_h = int(width * (h / w) * FONT_ASPECT)
    img = img.resize((width, new_h), Image.LANCZOS)
    pixels = list(img.getdata())
    chars = []
    for i, p in enumerate(pixels):
        idx = int(p / 255 * (len(ASCII_CHARS) - 1))
        chars.append(ASCII_CHARS[idx])
        if (i + 1) % width == 0:
            chars.append("\n")
    return "".join(chars).rstrip("\n").split("\n")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def dot_leader(label):
    """'Subject:' + dots, neofetch-style, e.g. 'Subject: ..............'"""
    text = f"{label}:"
    pad = max(3, DOTS_WIDTH - len(text))
    return text + " " + ("." * pad)


def build_panel_lines():
    panel_lines = []
    panel_lines.append(("handle", HANDLE))
    panel_lines.append(("divider", "-" * 40))
    for k, v in FIELDS_1.items():
        panel_lines.append(("field", (k, v)))
    panel_lines.append(("blank", ""))
    for k, v in FIELDS_2.items():
        panel_lines.append(("field", (k, v)))
    panel_lines.append(("blank", ""))
    panel_lines.append(("section", "Contact"))
    for k, v in CONTACT.items():
        panel_lines.append(("field", (k, v)))
    panel_lines.append(("blank", ""))
    panel_lines.append(("section", "GitHub Stats"))
    panel_lines.append(("stats", STATS_LINE_1))
    panel_lines.append(("stats", STATS_LINE_2))
    panel_lines.append(("stats", STATS_LINE_3))
    return panel_lines


def build_svg(art_lines):
    art_char_w = 3.6
    art_line_h = 7      # fixed — never distort the portrait's proportions
    panel_line_h = 15
    top_pad = 40

    panel_lines = build_panel_lines()

    art_h = len(art_lines) * art_line_h
    panel_h = len(panel_lines) * panel_line_h

    # Match heights by padding the shorter column with blank rows —
    # never by stretching/squishing the art or panel text.
    if art_h < panel_h:
        pad_rows = int((panel_h - art_h) / art_line_h)
        art_lines = list(art_lines) + [""] * pad_rows
        art_h = len(art_lines) * art_line_h
    elif panel_h < art_h:
        pad_rows = int((art_h - panel_h) / panel_line_h)
        panel_lines = panel_lines + [("blank", "")] * pad_rows
        panel_h = len(panel_lines) * panel_line_h

    art_px_w = int(max(len(l) for l in art_lines) * art_char_w)
    total_h = max(art_h, panel_h) + top_pad + 30
    total_w = art_px_w + 520 + 60
    panel_x = art_px_w + 70

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{total_w}" height="{total_h}" viewBox="0 0 {total_w} {total_h}">'
    ]
    svg_parts.append(f'''
  <style>
    .bg {{ fill: #0a0e12; }}
    .frame {{ fill:none; stroke:#1f6f6b; stroke-width:1.5; rx:8; }}
    .art {{ font-family: 'Courier New', monospace; font-size: 6px; fill: #35e0d0; white-space: pre; }}
    .handle {{ font-family: 'Courier New', monospace; font-size: 13px; fill: #35e0d0; font-weight:bold; }}
    .key {{ font-family: 'Courier New', monospace; font-size: 12px; fill: #35e0d0; }}
    .val {{ font-family: 'Courier New', monospace; font-size: 12px; fill: #cfe9e6; }}
    .section {{ font-family: 'Courier New', monospace; font-size: 12px; fill: #ff8a5c; font-weight:bold; }}
    .div {{ font-family: 'Courier New', monospace; font-size: 12px; fill: #1f6f6b; }}
  </style>
  <rect class="bg frame" x="1" y="1" width="{total_w - 2}" height="{total_h - 2}" />
''')

    # ASCII art block
    y = top_pad
    art_x = 30
    for line in art_lines:
        svg_parts.append(f'<text class="art" x="{art_x}" y="{y}" xml:space="preserve">{esc(line)}</text>')
        y += art_line_h

    # Info panel block
    y = top_pad
    for kind, content in panel_lines:
        if kind == "blank":
            pass
        elif kind == "handle":
            svg_parts.append(f'<text class="handle" x="{panel_x}" y="{y}">{esc(content)}</text>')
        elif kind == "divider":
            svg_parts.append(f'<text class="div" x="{panel_x}" y="{y}" xml:space="preserve">{esc(content)}</text>')
        elif kind == "section":
            svg_parts.append(f'<text class="section" x="{panel_x}" y="{y}">{esc(content)}</text>')
        elif kind == "stats":
            svg_parts.append(f'<text class="val" x="{panel_x}" y="{y}" xml:space="preserve">{esc(content)}</text>')
        elif kind == "field":
            k, v = content
            label = dot_leader(k)
            svg_parts.append(
                f'<text x="{panel_x}" y="{y}"><tspan class="key" xml:space="preserve">{esc(label)}</tspan>'
                f' <tspan class="val">{esc(v)}</tspan></text>'
            )
        y += panel_line_h

    svg_parts.append("</svg>")
    return "\n".join(svg_parts)


def main():
    if len(sys.argv) < 2:
        print("Usage: python profile_card.py <photo path>")
        sys.exit(1)
    art_lines = image_to_ascii(sys.argv[1])
    svg = build_svg(art_lines)
    with open("profile-card.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Wrote profile-card.svg")


if __name__ == "__main__":
    main()
