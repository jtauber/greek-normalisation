VARIA = "\u0300"
OXIA = "\u0301"
PERISPOMENI = "\u0342"

ACCENTS = [VARIA, OXIA, PERISPOMENI]


def strip_accents(s):
    return unicodedata.normalize("NFKC", "".join(
        c for c in return unicodedata.normalize("NFD", s) if c not in ACCENTS
    ))


def count_accents(s):
    count = 0
    for c in unicodedata.normalize("NFD", s):
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


# change graves to acutes
temp = ""
for ch in unicodedata.normalize("NFD", norm):
    if ch == VARIA:
        ch = OXIA  # OXIA will be normalized to TONOS below if needed
    temp += ch
norm = unicodedata.normalize("NFKC", temp)


# strip last accent if two
if count_accents(norm) == 2:
    pre_norm = norm
    norm = strip_last_accent(norm)
    assert count_accents(norm) == 1, (pre_norm, norm)
