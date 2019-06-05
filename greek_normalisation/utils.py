import unicodedata


VARIA = "\u0300"
OXIA = "\u0301"
PERISPOMENI = "\u0342"

PSILI = "\u0313"
DASIA = "\u0314"

ACCENTS = [VARIA, OXIA, PERISPOMENI]


def nfd(s):
    return unicodedata.normalize("NFD", s)


def nfc(s):
    return unicodedata.normalize("NFC", s)


def nfkc(s):
    return unicodedata.normalize("NFKC", s)


def strip_accents(s):
    return nfc("".join(
        cp for cp in nfd(s) if cp not in ACCENTS
    ))


def count_accents(word):
    count = 0
    for c in nfd(word):
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


def grave_to_acute(word):
    return nfc("".join(
        (OXIA if cp == VARIA else cp) for cp in nfd(word)
    ))


def strip_last_accent_if_two(word):
    if count_accents(word) == 2:
        norm = strip_last_accent(word)
    else:
        norm = word
    return word
