import re

import sys

import unicodedata

error_count = 0

with open("OCR Output Continuous text.txt") as f:
    for token in f.read().split():
        token = unicodedata.normalize("NFC", token).strip(".,;\u00B7\uFEFF")

        if token == "":
            continue

        if re.match(r"[\u0374\u0390-\u03A1\u03A3-\u03C1\u03C3-\u03CE\u1F00-\u1F15\u1F18-\u1F1D\u1F20-\u1F45\u1F48-\u1F4D\u1F50-\u1F57\u1F59\u1F5B\u1F5D\u1F5F-\u1F7D\u1F80-\u1FB4\u1FB6-\u1FBC\u1FC2-\u1FC4\u1FC6-\u1FCC\u1FD0-\u1FD3\u1FD6-\u1FDB\u1FE0-\u1FEC\u1FF2-\u1FF4\u1FF6-\u1FFC]+(\u2019|\u03C2)?$", token):

            breathing_error = False
            d = unicodedata.normalize("NFD", token.lower())
            if d[0] in "αεηιοω":
                if d[1] in "\u0313\u0314":
                    pass
                elif d[1] in "ιυ":
                    if d[2] in "\u0313\u0314":
                        pass
                    else:
                        breathing_error = True
                else:
                    breathing_error = True

            if breathing_error:
                error_count += 1

                print("*** ERROR ***", file=sys.stderr)
                print(token, file=sys.stderr)

                for ch in token:
                    print(ch, hex(ord(ch)), file=sys.stderr)
            else:
                print(token)
        else:
            error_count += 1

            print("*** ERROR ***", file=sys.stderr)
            print(token, file=sys.stderr)

            for ch in token:
                print(ch, hex(ord(ch)), file=sys.stderr)

    if error_count:
        print("***", error_count, "errors", file=sys.stderr)
