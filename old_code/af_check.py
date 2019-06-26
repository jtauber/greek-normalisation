#!/usr/bin/env python3

import glob
import re
import sys
import unicodedata


def error(*parts):
    print(": ".join(map(str, parts)), file=sys.stderr)


for fname in glob.glob("texts/*.txt"):

    with open(fname) as f:

        prev_ref = None

        for lnum, line in enumerate(f, 1):
            parts = line.strip().split()

            # there can be no blank lines

            if not parts:
                error(fname, lnum, "BLANK LINE")

            # tokens must be split by a single space

            if line != " ".join(parts) + "\n":
                error(fname, lnum, "BAD WHITESPACE")

            # the first token must be a reference of the form <num>.<num>
            # or <num>.<num>.<num>

            if not re.match(r"(\d+|EP|SB)\.\d+(\.\d+)?$", parts[0]):
                error(fname, lnum, "BAD REFERENCE FORM")

            # references must be in sort order

            ref = tuple(int({"EP": 999, "SB": 999}.get(i, i)) for i in parts[0].split("."))

            if prev_ref and ref <= prev_ref:
                error(fname, lnum, f"BAD REFERENCE ORDERING")

            prev_ref = ref

            for word in parts[1:]:

                # word must be NFC normalized

                if word != unicodedata.normalize("NFC", word):
                    error(fname, lnum, word, "BAD UNICODE NORMALIZATION")

                # word must contain value sequence of Greek characters

                if not re.match(WORD_REGEX, word):
                    error(fname, lnum, word, "BAD WORD")
                    for ch in word:
                        print("\t", ch, hex(ord(ch)), unicodedata.name(ch))

                # breathing must be correct (if not number or latin or uppercase)

                if (
                    not re.match(NUMBER, word) and
                    not re.match(LATIN, word) and
                    not word == word.upper()
                ):
                    d = unicodedata.normalize("NFD", word.lower())
                    if d[0] in "αεηιοω":
                        if d[1] in "\u0313\u0314":
                            pass
                        elif d[1] in "ιυ":
                            if d[2] in "\u0313\u0314":
                                pass
                            else:
                                error(fname, lnum, word, "BREATHING ERROR")
                        else:
                            error(fname, lnum, word, "BREATHING ERROR")
