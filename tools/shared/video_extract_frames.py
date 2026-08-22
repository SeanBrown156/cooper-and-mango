#!/usr/bin/env python3
"""Extract PNG frames from a video using ffmpeg."""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--fps", type=float, default=12)
    args = parser.parse_args()
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise SystemExit("ffmpeg is required for video frame extraction")
    args.output.mkdir(parents=True, exist_ok=True)
    pattern = str(args.output / "frame_%04d.png")
    subprocess.run([ffmpeg, "-y", "-i", str(args.video), "-vf", f"fps={args.fps}", pattern], check=True)
    print(f"Extracted video frames to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
