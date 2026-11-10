#!/usr/bin/env python3
"""Write themes/kanagawa-<variant>.css from the shared palette.

Usage: scripts/generate.py [path/to/palette.json]   (default: ../.github/palette.json)
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VARIANTS = ["wave", "dragon", "lotus"]


def roles(variant):
    """Map each role to its hex color; a role missing from the palette raises KeyError later."""
    return {role: c["hex"] for c in variant["colors"].values() for role in c["usage"]}

# GTK color name -> palette role.
COLORS = {
    "kanagawa_bg": "ui.float.bg",
    "kanagawa_fg": "ui.float.fg",
    "kanagawa_border": "ui.float.fg_border",
    "kanagawa_input_bg": "ui.bg_p1",
    "kanagawa_input_fg": "ui.fg",
    "kanagawa_selected_bg": "ui.pmenu.bg_sel",
    "kanagawa_selected_fg": "ui.pmenu.fg",
    "kanagawa_match": "syn.fun",
}
RULES = """
window {
  background-color: @kanagawa_bg;
  border: 1px solid @kanagawa_border;
}

#input {
  color: @kanagawa_input_fg;
  background-color: @kanagawa_input_bg;
  border: none;
}

#inner-box,
#outer-box,
#scroll,
#entry {
  background-color: @kanagawa_bg;
}

#text {
  color: @kanagawa_fg;
}

#entry:selected {
  background-color: @kanagawa_selected_bg;
}

#entry:selected #text {
  color: @kanagawa_selected_fg;
}
"""


def theme(variant, colors):
    out = [f"/* Kanagawa {variant.capitalize()} */", "/* https://github.com/kanagawa-community/wofi */", ""]
    out += [f"@define-color {k} {colors[r]};" for k, r in COLORS.items()]
    return "\n".join(out) + "\n" + RULES


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / ".github" / "palette.json"
    variants = json.loads(path.read_text())["variants"]
    for v in VARIANTS:
        out = ROOT / "themes" / f"kanagawa-{v}.css"
        out.parent.mkdir(exist_ok=True)
        out.write_text(theme(v, roles(variants[v])))
        print(out.relative_to(ROOT))


if __name__ == "__main__":
    main()
