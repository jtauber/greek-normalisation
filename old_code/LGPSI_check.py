#!/usr/bin/env python3

import codecs
import collections
import glob
import re
import unicodedata

from normalise import convert


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
