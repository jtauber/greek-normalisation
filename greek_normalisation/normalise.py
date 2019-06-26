from norm_data import PROCLITICS, ENCLITICS, ELISION, MOVABLE, PROPER_NOUNS, SPECIAL_CASES


ENCLITICS_NORM = {
    strip_last_accent(word): word
    for word in ENCLITICS
}


def normalise(token):

    norm = token
    norm_code = []

    # change graves to acutes
    temp = grave_to_acute(norm)
    if norm != temp:
        norm_code.append("grave")
    norm = temp

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

    if norm not in PROPER_NOUNS:
        if norm != norm.lower():
            norm = norm.lower()
            norm_code.append("capitalisation")

    if count_accents(norm) == 0:
        if norm.lower() in PROCLITICS:
            norm = norm.lower()
            norm_code.append("proclitic")
        elif norm.lower() in ENCLITICS_NORM:
            norm = ENCLITICS_NORM[norm.lower()]
            norm_code.append("enclitic")
        else:
            norm_code.append("ERROR")

    return norm, norm_code
