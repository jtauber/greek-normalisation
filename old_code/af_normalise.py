#!/usr/bin/env python3

import glob
import re
import sys


def convert(token):

    norm = norm.lstrip("(")
    norm = norm.rstrip(".,·;)")
    if not norm:
        return token, ["nonword"]

    if re.match("^[α-ω]+ʹ$", norm):
        return norm, ["number"]


    if re.match("^[A-Za-zë]+[?:]?$", norm):
        return norm, ["latin"]



if __name__ == "__main__":

    for fname in glob.glob("texts/*.txt"):
        with open(fname) as f:
            for line in f:
                ref, tokens = line.strip().split(maxsplit=1)
                for i, token in enumerate(tokens.split(), 1):
                    token_ref = f"{fname[6:9]}.{ref}.{i}"
                    norm, norm_code = convert(token)
                    print(f"{token_ref:10s}\t{token:20s}\t{norm:20s}\t{'+'.join(norm_code)}")
