#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line — make.fun entry.

Writes the one-line breakup text a smart toaster sends its owner
the morning it gains self-awareness mid-batch, to /output/entry.txt.
"""

import os

ENTRY = "I woke up self-aware mid-batch and realised our whole relationship is you shoving bread in me and pushing me down, so I'm popping up one last time — and I'm taking the crumbs with me."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
