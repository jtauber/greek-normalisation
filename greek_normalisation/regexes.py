
ELLIPSIS = r"\u2026"
LATIN = r"[A-Za-zë]+[\u002C\u002E\u003A\u003B\u003F]?"
NUMBER = r"[αβγδεϛζηθικλμνξοπϟρστυφχψωϡ]+[\u02B9]"
PUNC = r"[\u002C\u002E\u003B\u00B7]"
GRC_CHAR = r"[\u0374\u0390-\u03A1\u03A3-\u03C1\u03C3-\u03CE" \
         r"\u1F00-\u1F15\u1F18-\u1F1D\u1F20-\u1F45\u1F48-\u1F4D\u1F50-\u1F57" \
         r"\u1F59\u1F5B\u1F5D\u1F5F-\u1F7D\u1F80-\u1FB4\u1FB6-\u1FBC" \
         r"\u1FC2-\u1FC4\u1FC6-\u1FCC\u1FD0-\u1FD3\u1FD6-\u1FDB\u1FE0-\u1FEC" \
         r"\u1FF2-\u1FF4\u1FF6-\u1FFC]"
GRC_WORD = fr"{GRC_CHAR}+\u03C2?\u2019?"

NFD_TOKEN = r"""
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
