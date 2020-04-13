from enum import Flag, auto

from .norm_data import PROCLITICS, ENCLITICS, ELISION, MOVABLE
from .utils import (
    strip_last_accent, grave_to_acute, strip_last_accent_if_two, count_accents
)

ENCLITICS_NORM = {
    strip_last_accent(word): word
    for word in ENCLITICS
}


class Norm(Flag):
    UNCHANGED = 0
    GRAVE = auto()
    ELISION = auto()
    MOVABLE = auto()
    EXTRA = auto()
    CAPITALISED = auto()
    PROCLITIC = auto()
    ENCLITIC = auto()
    NO_ACCENT = auto()
    ALL = (
        GRAVE | ELISION | MOVABLE | EXTRA | CAPITALISED |
        PROCLITIC | ENCLITIC | NO_ACCENT
    )


class Normaliser:

    def __init__(self, config=Norm.ALL, proper_nouns=set()):
        self.config = config
        self.proper_nouns = proper_nouns

    def normalise(self, token):

        norm = token
        norm_code = Norm.UNCHANGED

        if self.config & Norm.GRAVE:
            # change graves to acutes
            temp = grave_to_acute(norm)
            if norm != temp:
                norm_code |= Norm.GRAVE
            norm = temp

        if self.config & Norm.ELISION:
            if norm in ELISION:
                norm = ELISION[norm]
                norm_code |= Norm.ELISION

        if self.config & Norm.MOVABLE:
            if norm in MOVABLE:
                norm = MOVABLE[norm]
                norm_code |= Norm.MOVABLE

        if self.config & Norm.EXTRA:
            # strip last accent if two
            temp = strip_last_accent_if_two(norm)
            if norm != temp:
                norm_code |= Norm.EXTRA
            norm = temp

        if self.config & Norm.CAPITALISED:
            if norm not in self.proper_nouns:
                if norm != norm.lower():
                    norm = norm.lower()
                    norm_code |= Norm.CAPITALISED

        if count_accents(norm) == 0:
            if norm.lower() in PROCLITICS:
                if self.config & Norm.PROCLITIC:
                    norm = norm.lower()
                    norm_code |= Norm.PROCLITIC
            elif norm.lower() in ENCLITICS_NORM:
                if self.config & Norm.ENCLITIC:
                    norm = ENCLITICS_NORM[norm.lower()]
                    norm_code |= Norm.ENCLITIC
            else:
                if self.config & Norm.NO_ACCENT:
                    norm_code |= Norm.NO_ACCENT

        return norm, norm_code
