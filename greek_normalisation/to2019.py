#!/usr/bin/env python3

import fileinput
import sys


CHARACTERS_TO_CHANGE = [
    "\u02BC",
    "\u1FBF",
]

lines_changed = 0

with fileinput.input() as f:
    for line in f:
        text = line
        for ch in CHARACTERS_TO_CHANGE:
            text = text.replace(ch, "\u2019")
        print(text, end="")
        if text != line:
            lines_changed += 1

print(f"{lines_changed} lines changed", file=sys.stderr)
