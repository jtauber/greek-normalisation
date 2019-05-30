#!/usr/bin/env python3

import codecs
import collections
import glob
import re
import unicodedata

from normalise import convert


TOKEN_REGEX = r"""
[
    \u0028              # (
    \u00AB              # «
]?
(?P<word>
    [
        \u0300          # combining grave
        \u0301          # combining acute
        \u0304          # combining macron
        \u0308          # combining diaeresis
        \u0313          # combining smooth breathing
        \u0314          # combining rough breathing
        \u0342          # combining circumflex
        \u0345          # combining iota subscript
        \u0391-\u03A9   # uppercase
        \u03B1-\u03C9   # lowercase
        \u002D          # - (hyphen)
    ]+
[
    \u2019              # ’ (apostrophe)
]?
)
[
    \u0021              # !
    \u0029              # )
    \u002C              # ,
    \u002E              # .
    \u003B              # ;
    \u00B7              # · (middle dot)
    \u00BB              # »
]*
$
"""

c = collections.Counter()

for FILENAME in glob.glob("src/*.md"):
    with codecs.open(FILENAME, "r", encoding="utf-8-sig") as f:
        for LINE_NUM, line in enumerate(f, 1):
            for TOKEN_NUM, token in enumerate(line.split(), 1):
                token = unicodedata.normalize("NFD", token)
                if token in ["#", "##"]:
                    pass
                elif token == "...":
                    pass
                elif re.match("[CDI]+", token):
                    pass
                else:
                    m = re.match(TOKEN_REGEX, token, re.VERBOSE)
                    if m:
                        word = unicodedata.normalize("NFC", m.groupdict()["word"])
                        if word == "ἀλλα":
                            print(FILENAME, LINE_NUM, TOKEN_NUM, token, [hex(ord(ch)) for ch in token])
                            quit()
                        c[word] += 1
                    else:
                        print("INVALID TOKEN:")
                        print(FILENAME, LINE_NUM, TOKEN_NUM, token, [hex(ord(ch)) for ch in token])
                        quit()

for word, count in c.most_common():
    norm, reasons = convert(word)
    # print(norm, word, reasons)
    if "ERROR" in reasons:
        print('    "' + word + '",')
