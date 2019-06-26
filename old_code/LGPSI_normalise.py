#!/usr/bin/env python3

import glob
import re
import sys


def convert(token):

    norm = norm.lstrip("(")
    norm = norm.rstrip(".,·;)")
    if not norm:
        return token, ["nonword"]

    if norm in SPECIAL_CASES:
        return norm, ["special"]

    if re.match("^[α-ω]+ʹ$", norm):
        return norm, ["number"]

    if re.match("^[A-Za-zë]+[?:]?$", norm):
        return norm, ["latin"]
