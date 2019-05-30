#!/usr/bin/env python3

import sys
import unicodedata

from data import PROCLITICS, ENCLITICS, ELISION, MOVABLE, PROPER_NOUNS

VARIA = "\u0300"
OXIA = "\u0301"
PSILI = "\u0313"
DASIA = "\u0314"
PERISPOMENI = "\u0342"

ACCENTS = [VARIA, OXIA, PERISPOMENI]


def d(s):
    return unicodedata.normalize("NFD", s)


def n(x):
    return unicodedata.normalize("NFKC", x)


def strip_accents(s):
    return n("".join(
        c for c in d(s) if c not in ACCENTS
    ))


def count_accents(s):
    count = 0
    for c in d(s):
        if c in ACCENTS:
            count += 1
    return count


def strip_last_accent(word):
    x = list(word)
    for i, ch in enumerate(x[::-1]):
        s = strip_accents(ch)
        if s != ch:
            x[-i - 1] = s
            break
    return "".join(x)


ENCLITICS_NORM = {
    strip_last_accent(word): word
    for word in ENCLITICS
}

def convert(token):

    norm = token
    norm_code = []

    # change graves to acutes
    temp = ""
    for ch in d(norm):
        if ch == VARIA:
            ch = OXIA  # OXIA will be normalized to TONOS below if needed
        temp += ch
    if norm != n(temp):
        norm_code.append("grave")
    norm = n(temp)

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

    if count_accents(norm) == 2:
        pre_norm = norm
        norm = strip_last_accent(norm)
        assert count_accents(norm) == 1, (pre_norm, norm)
        norm_code.append("extra")

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
