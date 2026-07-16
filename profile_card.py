"""
Generates profile-card.svg — a neofetch-style terminal card: a halftone
dot-grid portrait on the left, dot-leader info panel on the right.
Matches the KARTHIK1749/KARTHIK1749 reference layout (same sections/order),
filled in with your own info and photo.

The portrait uses a halftone dot grid (variable dot size per pixel) rather
than character-ramp ASCII art — this reads far more clearly as a face at
the same physical size.

Usage:
    python profile_card.py photo.jpg

Requires:
    pip install pillow
"""

import sys
from PIL import Image, ImageOps, ImageFilter

# ---------------- Your info ----------------
HANDLE = "Ali@Neural-Grid"

FIELDS_1 = {
    "Subject": "Ali Asghar",
    "Role": "AI/ML Engineer & Full-Stack Dev",
    "Origin": "Naushero Feroze, Pakistan",
    "Education": "CS Student, NED University",
    "Experience": "3+ years",
    "Status": "Building . Learning . Shipping",
    "ToolChain": "VS Code, Git, GitHub, Postman",
}

FIELDS_2 = {
    "Neural.Core": "Python, JavaScript, TypeScript",
    "Neural.AI": "ML, Deep Learning, CV, NLP, GenAI",
    "Neural.Frontend": "React, Next.js, HTML/CSS, Tailwind",
    "Neural.Backend": "Node.js, Express, Django, Flask",
    "Neural.Stack": "MERN, Django, Flask",
    "Neural.DB": "MongoDB, PostgreSQL, MySQL, Redis",
}

ABOUT = {
    "Currently.Learning": "Django, TensorFlow",
    "Collab.Interest": "DevOps, Open Source, AI Projects",
    "Off.Grid": "Writes Urdu poetry",
}

CONTACT = {
    "Grid.Mail": "aliasghargh540@gmail.com",
    "Grid.Portfolio": "portfolio-asghar-ali.vercel.app",
    "Grid.LinkedIn": "ali-asghar-a730322bb",
    "Grid.Github": "AsgharGhanghro",
}

DOTS_WIDTH = 22    # how many dot-leader characters to draw in labels

# ---- Halftone portrait settings ----
GRID_W = 130        # dot columns — higher = more recognizable detail
DOT_PITCH = 3.6      # px between dot centers
MAX_DOT_R = 1.85     # px, largest dot radius (brightest pixel)
MIN_DOT_R = 0.0       # px, darkest pixels get no dot at all
DARK_CUTOFF = 0.12    # brightness below this = no dot (true black)
DOT_COLOR = "#40e0e0"


def image_to_dot_grid(path, grid_w=GRID_W):
    """Convert a photo into a halftone dot grid of (col, row, radius)."""
    img = Image.open(path).convert("L")
    img = ImageOps.autocontrast(img, cutoff=1)
    img = img.filter(ImageFilter.GaussianBlur(1.3))  # suppress thin watermark/logo linework

    # Known faint watermark/logo mark in the corner of this particular photo —
    # force it to black so it never renders as a stray dot in the background.
    from PIL import ImageDraw
    draw = ImageDraw.Draw(img)
    w0, h0 = img.size
    draw.rectangle([w0 * 0.60, 0, w0, h0 * 0.28], fill=0)

    w, h = img.size
    grid_h = int(grid_w * (h / w))
    img = img.resize((grid_w, grid_h), Image.LANCZOS)
    pixels = list(img.getdata())

    dots = []
    for i, p in enumerate(pixels):
        col = i % grid_w
        row = i // grid_w
        brightness = p / 255  # bright pixel = more cyan ink; dark = recedes to black
        if brightness < DARK_CUTOFF:
            radius = 0.0
        else:
            norm = (brightness - DARK_CUTOFF) / (1 - DARK_CUTOFF)
            radius = MIN_DOT_R + norm * (MAX_DOT_R - MIN_DOT_R)
        dots.append((col, row, radius))
    return dots, grid_w, grid_h


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
    panel_lines.append(("section", "About"))
    for k, v in ABOUT.items():
        panel_lines.append(("field", (k, v)))
    panel_lines.append(("blank", ""))
    panel_lines.append(("section", "Contact"))
    for k, v in CONTACT.items():
        panel_lines.append(("field", (k, v)))
    return panel_lines


def build_svg(dots, grid_w, grid_h):
    panel_line_h = 15
    top_pad = 40

    panel_lines = build_panel_lines()

    art_px_w = grid_w * DOT_PITCH
    art_px_h = grid_h * DOT_PITCH
    panel_h = len(panel_lines) * panel_line_h

    # Pad the shorter column with blank space so both columns end at the
    # same height, without distorting the portrait's proportions.
    extra_rows = 0
    if art_px_h < panel_h:
        extra_rows = int((panel_h - art_px_h) / DOT_PITCH)
    elif panel_h < art_px_h:
        pad_rows = int((art_px_h - panel_h) / panel_line_h)
        panel_lines = panel_lines + [("blank", "")] * pad_rows
        panel_h = len(panel_lines) * panel_line_h

    total_art_h = (grid_h + extra_rows) * DOT_PITCH
    total_h = max(total_art_h, panel_h) + top_pad + 30
    total_w = art_px_w + 520 + 60
    panel_x = art_px_w + 90
    art_x0 = 30
    art_y0 = top_pad

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{total_w:.0f}" height="{total_h:.0f}" viewBox="0 0 {total_w:.0f} {total_h:.0f}">'
    ]
    svg_parts.append(f'''
  <style>
    .bg {{ fill: #0a0e12; }}
    .frame {{ fill:none; stroke:#1f6f6b; stroke-width:1.5; rx:8; }}
    .handle {{ font-family: 'Courier New', monospace; font-size: 13px; fill: #40e0e0; font-weight:bold; }}
    .key {{ font-family: 'Courier New', monospace; font-size: 12px; fill: #40e0e0; }}
    .val {{ font-family: 'Courier New', monospace; font-size: 12px; fill: #cfe9e6; }}
    .section {{ font-family: 'Courier New', monospace; font-size: 12px; fill: #ff8a5c; font-weight:bold; }}
    .div {{ font-family: 'Courier New', monospace; font-size: 12px; fill: #1f6f6b; }}
  </style>
  <rect class="bg frame" x="1" y="1" width="{total_w - 2:.0f}" height="{total_h - 2:.0f}" />
''')

    # Halftone dot portrait
    dot_parts = [f'<g fill="{DOT_COLOR}">']
    for col, row, radius in dots:
        if radius < 0.05:
            continue
        cx = art_x0 + col * DOT_PITCH
        cy = art_y0 + row * DOT_PITCH
        dot_parts.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{radius:.2f}"/>')
    dot_parts.append('</g>')
    svg_parts.append("".join(dot_parts))

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
    dots, grid_w, grid_h = image_to_dot_grid(sys.argv[1])
    svg = build_svg(dots, grid_w, grid_h)
    with open("profile-card.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Wrote profile-card.svg")


if __name__ == "__main__":
    main()
