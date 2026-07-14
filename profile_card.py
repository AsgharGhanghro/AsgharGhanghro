"""
Generates profile-card.svg: an ASCII-art portrait (from a photo) next to a
neofetch-style terminal info panel, in the cyan-on-black terminal aesthetic.

Usage:
    python profile_card.py photo.jpg

Requires:
    pip install pillow
"""

import sys
from PIL import Image

# ---------------- Your info ----------------
INFO = {
    "handle": "Asghar@Neural-Grid",
    "Subject": "Ali Asghar",
    "Role": "AI/ML Engineer",
    "Origin": "Naushero Feroze, Sindh, Pakistan",
    "Status": "Building - Learning - Shipping",
    "ToolChain": "VS Code, Git, GitHub, Postman",
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

# GitHub Stats — fill in manually, or wire up a GitHub Actions step that
# fetches these via the API (see README notes) and rewrites this dict.
STATS = {
    "Repos": "-",
    "Commits": "-",
    "Stars": "-",
    "Followers": "-",
}
# --------------------------------------------

ASCII_CHARS = "@%#*+=-:. "
ART_WIDTH = 110   # characters wide — higher = more recognizable detail
FONT_ASPECT = 0.5  # monospace chars are taller than wide


def image_to_ascii(path, width=ART_WIDTH):
    from PIL import ImageOps
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


def build_svg(art_lines):
    art_char_w = 3.6
    art_line_h = 7
    line_h = 14  # panel line height
    art_px_w = int(max(len(l) for l in art_lines) * art_char_w)
    art_px_h = len(art_lines) * art_line_h

    panel_lines = []
    panel_lines.append(("handle", INFO["handle"]))
    panel_lines.append(("divider", "-" * 34))
    for k in ["Subject", "Role", "Origin", "Status", "ToolChain"]:
        panel_lines.append(("field", (k, INFO[k])))
    panel_lines.append(("divider", ""))
    for k in ["Neural.Core", "Neural.AI", "Neural.Frontend", "Neural.Backend", "Neural.Stack"]:
        panel_lines.append(("field", (k, INFO[k])))
    panel_lines.append(("section", "Contact"))
    for k, v in CONTACT.items():
        panel_lines.append(("field", (k, v)))
    panel_lines.append(("section", "GitHub Stats"))
    panel_lines.append(("stats",
        f"Repos: {STATS['Repos']}   Stars: {STATS['Stars']}   Followers: {STATS['Followers']}   Commits: {STATS['Commits']}"))

    panel_px_h = len(panel_lines) * line_h + 30
    total_h = max(art_px_h, panel_px_h) + 60
    total_w = art_px_w + 480 + 60

    svg_parts = []
    svg_parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{total_w}" height="{total_h}" viewBox="0 0 {total_w} {total_h}">'
    )
    svg_parts.append(f'''
  <style>
    .bg {{ fill: #0a0e12; }}
    .frame {{ fill:none; stroke:#1f6f6b; stroke-width:1.5; rx:8; }}
    .art {{ font-family: 'Courier New', monospace; font-size: 6px; fill: #35e0d0; white-space: pre; }}
    .handle {{ font-family: 'Courier New', monospace; font-size: 13px; fill: #35e0d0; font-weight:bold; }}
    .key {{ font-family: 'Courier New', monospace; font-size: 12px; fill: #7fdad3; }}
    .val {{ font-family: 'Courier New', monospace; font-size: 12px; fill: #cfe9e6; }}
    .section {{ font-family: 'Courier New', monospace; font-size: 12px; fill: #ff8a5c; font-weight:bold; }}
    .div {{ font-family: 'Courier New', monospace; font-size: 12px; fill: #1f6f6b; }}
  </style>
  <rect class="bg frame" x="1" y="1" width="{total_w - 2}" height="{total_h - 2}" />
''')

    # ASCII art block
    y = 40
    art_x = 30
    for line in art_lines:
        svg_parts.append(f'<text class="art" x="{art_x}" y="{y}" xml:space="preserve">{esc(line)}</text>')
        y += art_line_h

    # Info panel block
    panel_x = art_px_w + 70
    y = 40
    for kind, content in panel_lines:
        if kind == "handle":
            svg_parts.append(f'<text class="handle" x="{panel_x}" y="{y}">{esc(content)}</text>')
        elif kind == "divider":
            svg_parts.append(f'<text class="div" x="{panel_x}" y="{y}" xml:space="preserve">{esc(content)}</text>')
        elif kind == "section":
            svg_parts.append(f'<text class="section" x="{panel_x}" y="{y}">{esc(content)}</text>')
        elif kind == "stats":
            svg_parts.append(f'<text class="val" x="{panel_x}" y="{y}">{esc(content)}</text>')
        elif kind == "field":
            k, v = content
            label = f"{k}:".ljust(18)
            svg_parts.append(
                f'<text x="{panel_x}" y="{y}"><tspan class="key" xml:space="preserve">{esc(label)}</tspan>'
                f'<tspan class="val">{esc(v)}</tspan></text>'
            )
        y += line_h

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
