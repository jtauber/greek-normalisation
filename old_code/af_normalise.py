#!/usr/bin/env python3

import glob
import re
import sys

from norm_data import PROCLITICS, ENCLITICS, ELISION, MOVABLE, PROPER_NOUNS


ENCLITICS_NORM = {
    strip_last_accent(word): word
    for word in ENCLITICS
}

def convert(token):

    norm = token
    norm = norm.lstrip("(")
    norm = norm.rstrip(".,·;)")
    if not norm:
        return token, ["nonword"]

    if re.match("^[α-ω]+ʹ$", norm):
        return norm, ["number"]


    if re.match("^[A-Za-zë]+[?:]?$", norm):
        return norm, ["latin"]

    norm_code = []

    # change graves to acutes
    temp = grave_to_acute(norm)
    if norm != temp:
        norm_code.append("grave")
    norm = temp

    if norm not in PROPER_NOUNS:
        if norm != norm.lower():
            norm = norm.lower()
            norm_code.append("capitalisation")

    if norm in ELISION:
        norm = ELISION[norm]
        norm_code.append("elision")

    if norm in MOVABLE:
        norm = MOVABLE[norm]
        norm_code.append("movable")

    # strip last accent if two
    temp = strip_last_accent_if_two(norm)
    if norm != temp:
        norm_code.append("extra")
    norm = temp

    if count_accents(norm) == 0:
        if norm.lower() in PROCLITICS:
            norm = norm.lower()
            norm_code.append("proclitic")
        elif norm.lower() in ENCLITICS_NORM:
            norm = ENCLITICS_NORM[norm.lower()]
            norm_code.append("enclitic")
        elif norm in [  # known bugs
        ]:
            norm_code.append("bug?")
        else:
            norm_code.append("ERROR")

    return norm, norm_code


if __name__ == "__main__":

    for fname in glob.glob("texts/*.txt"):
        with open(fname) as f:
            for line in f:
                ref, tokens = line.strip().split(maxsplit=1)
                for i, token in enumerate(tokens.split(), 1):
                    token_ref = f"{fname[6:9]}.{ref}.{i}"
                    norm, norm_code = convert(token)
                    print(f"{token_ref:10s}\t{token:20s}\t{norm:20s}\t{'+'.join(norm_code)}")
