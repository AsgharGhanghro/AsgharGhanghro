"""
Generates dark.svg and light.svg — an ASCII-art banner with your name,
styled for GitHub's automatic dark/light theme switching (via <picture>).

Usage:
    python ascii_to_svg.py

Requires:
    pip install pyfiglet
"""

import pyfiglet

# ---- Customize these ----
NAME = "Asghar Ghangro"
FIGLET_FONT = "big"        # try: slant, standard, big, small, banner3-D
TAGLINE = "AI/ML Engineer  |  Full-Stack Developer"
# --------------------------

THEMES = {
    "dark": {
        "bg": "#0d1117",
        "text": "#58a6ff",
        "tagline": "#8b949e",
        "border": "#30363d",
    },
    "light": {
        "bg": "#ffffff",
        "text": "#0969da",
        "tagline": "#57606a",
        "border": "#d0d7de",
    },
}


def build_svg(theme_name: str) -> str:
    theme = THEMES[theme_name]
    art = pyfiglet.figlet_format(NAME, font=FIGLET_FONT)
    lines = art.rstrip("\n").split("\n")

    char_w = 9.2
    line_h = 20
    max_len = max(len(line) for line in lines)
    width = int(max_len * char_w) + 80
    height = line_h * len(lines) + 100

    svg_lines = []
    y = 60
    for line in lines:
        escaped = (
            line.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )
        svg_lines.append(
            f'<text x="40" y="{y}" xml:space="preserve">{escaped}</text>'
        )
        y += line_h

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <style>
    .bg {{ fill: {theme["bg"]}; }}
    text {{
      font-family: 'Courier New', Consolas, monospace;
      font-size: 15px;
      fill: {theme["text"]};
      white-space: pre;
    }}
    .tagline {{
      font-family: 'Fira Code', Consolas, monospace;
      font-size: 14px;
      fill: {theme["tagline"]};
    }}
    rect.frame {{
      fill: none;
      stroke: {theme["border"]};
      stroke-width: 1.5;
      rx: 10;
    }}
  </style>
  <rect class="bg frame" x="1" y="1" width="{width - 2}" height="{height - 2}" />
  {"".join(svg_lines)}
  <text class="tagline" x="40" y="{y + 20}">{TAGLINE}</text>
</svg>'''
    return svg


def main():
    for theme_name in THEMES:
        svg = build_svg(theme_name)
        out_path = f"{theme_name}.svg"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
