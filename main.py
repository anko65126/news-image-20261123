#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261123 bounty.

The artwork itself lives next to this file as entry.png: a single
front-page collage covering the COP31 collapse in Antalya, the drone
strikes reported at sea and over Ukraine, the record opening day of
GTA VI, and the United States House result, all from 23 November 2026.

Grading runs this file twice in a sandbox without network access and
compares the two outputs byte for byte, so the safest program is one
that simply publishes the stored artwork, unchanged, every time.
"""
from pathlib import Path

ARTWORK = Path(__file__).resolve().with_name("entry.png")
DESTINATION_FOLDER = Path("/output")
DESTINATION_FILE = DESTINATION_FOLDER / "entry.png"


def publish() -> None:
    payload = ARTWORK.read_bytes()
    DESTINATION_FOLDER.mkdir(parents=True, exist_ok=True)
    DESTINATION_FILE.write_bytes(payload)
    written_back = DESTINATION_FILE.read_bytes()
    if written_back != payload:
        raise SystemExit("output does not match entry.png byte for byte")


if __name__ == "__main__":
    publish()
