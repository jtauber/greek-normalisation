#!/usr/bin/env python3

import sys

from data import PROCLITICS, ENCLITICS, ELISION, MOVABLE, PROPER_NOUNS


ENCLITICS_NORM = {
    strip_last_accent(word): word
    for word in ENCLITICS
}

def convert(token):

    norm = token
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
            print("*** ERROR ***", file=sys.stderr)
            print(norm, file=sys.stderr)

    return norm, norm_code


if __name__ == "__main__":
    with open("tokens.txt") as f:
        for line in f:
            token = line.strip()
            norm, norm_code = convert(token)
            print(f"{token:20s}\t{norm:20s}\t{'+'.join(norm_code)}")
