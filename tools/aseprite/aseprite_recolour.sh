#!/bin/sh
set -eu

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <input-wip-image-or-aseprite> <output-wip-image-or-aseprite>" >&2
  exit 2
fi

input=$1
output=$2
aseprite_path=${ASEPRITE_PATH:-/Applications/Aseprite.app/Contents/MacOS/aseprite}
palette_path=${CM_MASTER_PALETTE:-assets/palette/cooper_mango_master_palette.gpl}

case "$input" in
  */wip/*) ;;
  *) echo "Refusing to recolour outside a package wip/ folder: $input" >&2; exit 2 ;;
esac
case "$output" in
  */wip/*) ;;
  *) echo "Refusing to write recoloured output outside a package wip/ folder: $output" >&2; exit 2 ;;
esac
[ -x "$aseprite_path" ] || { echo "Aseprite not found: $aseprite_path" >&2; exit 1; }
[ -f "$palette_path" ] || { echo "Palette not found: $palette_path" >&2; exit 1; }
[ "$input" != "$output" ] || { echo "Input and output must be different paths" >&2; exit 2; }

mkdir -p "$(dirname "$output")"
"$aseprite_path" -b "$input" --palette "$palette_path" --save-as "$output"
echo "Recoloured $input -> $output using $palette_path"
