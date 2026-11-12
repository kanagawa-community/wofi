# Window hook for .github/scripts/capture-windows.sh: Wofi opens with each theme and a
# fixed list, so the window, the input, the entries and the selected entry show.
# It is a pop-up, so it gets no window frame.
# Requires: wofi.
# shellcheck shell=bash
name=Wofi
frame=none
size=600x360

launch() {
  printf 'The Great Wave off Kanagawa\nFine Wind, Clear Morning\nThunderstorm Beneath the Summit\nEjiri in Suruga Province\nKajikazawa in Kai Province\nMishima Pass in Kai Province\n' \
    >"$work/prints.txt"
  printf 'sh -c "wofi --dmenu --conf /dev/null --style %s --width 600 --height 360 --prompt prints < %s"' \
    "$root/themes/kanagawa-$1.css" "$work/prints.txt"
}
