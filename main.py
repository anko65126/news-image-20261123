#!/usr/bin/env python3
"""Writes the entry image for make.fun bounty news-image-20261123.

The image (entry.png, held in this repository) sums up the world news of
23 November 2026 in one picture: the COP31 climate summit collapse in
Antalya, drone warfare at sea and over Ukraine, GTA VI's record first-day
revenue, and the Democrats taking the US House.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"), os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
