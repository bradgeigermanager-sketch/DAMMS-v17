#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def explode_bundle(bundle_path: str):
    current_path = None
    current_lines = []

    with open(bundle_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("===FILE: "):
                if current_path is not None:
                    write_file(current_path, current_lines)
                current_path = line.strip().split("===FILE: ", 1)[1]
                current_lines = []
            elif line.startswith("===END_FILE"):
                if current_path is not None:
                    write_file(current_path, current_lines)
                    current_path = None
                    current_lines = []
            else:
                if current_path is not None:
                    current_lines.append(line)

    if current_path is not None:
        write_file(current_path, current_lines)

def write_file(rel_path: str, lines):
    path = Path(rel_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tools/explode_repo.py damms_v17_repo_bundle.txt")
        sys.exit(1)
    explode_bundle(sys.argv[1])
