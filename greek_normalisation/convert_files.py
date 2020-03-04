#!/usr/bin/env python3

import fileinput
import sys

from .utils import nfc, nfd, convert_to_2019


def convert(func):
    lines_changed = 0

    with fileinput.input() as f:
        for line in f:
            text = func(line)
            print(text, end="")
            if text != line:
                lines_changed += 1

    print(f"{lines_changed} lines changed", file=sys.stderr)


def to_nfc():
    convert(nfc)


def to_nfd():
    convert(nfd)


def to_2019():
    convert(convert_to_2019)
