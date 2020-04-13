Tests
=====

    This is a literate doctest.
    Run ``python3 -m doctest -v tests.rst`` to test.

greek_normalisation.utils
-------------------------

>>> from greek_normalisation.utils import (
...     nfd, nfc, nfkc,
...     strip_accents, count_accents, strip_last_accent, grave_to_acute,
...     strip_last_accent_if_two, breathing_check
... )

>>> len(nfd('ἄ'))
3

>>> len(nfc('ἄ'))
1

>>> nfkc('\u03D5') == nfkc('\u03C6')
True

>>> strip_accents('μῆνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος')
'μηνιν ἀειδε θεα Πηληϊαδεω Ἀχιληος'

>>> [count_accents(word) for word in 'τὴν γυναῖκά σου'.split()]
[1, 2, 0]

>>> strip_last_accent('γυναῖκά')
'γυναῖκα'

but

>>> strip_last_accent('τὴν')
'την'

which might not be what you want, so:

>>> strip_last_accent_if_two('γυναῖκά')
'γυναῖκα'

and

>>> strip_last_accent_if_two('τὴν')
'τὴν'

>>> grave_to_acute('τὴν')
'τήν'

>>> breathing_check('αβ')
False

>>> breathing_check('ἀβ')
True

>>> breathing_check('αι')
False

>>> breathing_check('ἀι')
False

>>> breathing_check('ἀϊ')
True

>>> breathing_check('ἀε')
True

>>> breathing_check('αἰ')
True

>>> breathing_check('β')
True

>>> breathing_check('α')
False

>>> breathing_check('ἀ')
True


normalise
---------

>>> from greek_normalisation.normalise import Normaliser, Norm

>>> normalise = Normaliser().normalise

>>> normalise('τὴν')
('τήν', <Norm.GRAVE: 1>)

>>> normalise('γυναῖκά')
('γυναῖκα', <Norm.EXTRA: 8>)

>>> normalise('σου')
('σου', <Norm.ENCLITIC: 64>)

>>> normalise('Τὴν')
('τήν', <Norm.CAPITALISED|GRAVE: 17>)

>>> normalise('ὁ')
('ὁ', <Norm.PROCLITIC: 32>)

>>> normalise('ὁς')
('ὁς', <Norm.NO_ACCENT: 128>)

>>> normalise('μετ’')
('μετά', <Norm.ELISION: 2>)

>>> normalise('οὐκ')
('οὐ', <Norm.PROCLITIC|MOVABLE: 36>)

>>> normalise('Ἀχιλλεύς')
('ἀχιλλεύς', <Norm.CAPITALISED: 16>)

>>> PROPER_NOUNS = {'Ἀχιλλεύς'}
>>> normalise = Normaliser(proper_nouns=PROPER_NOUNS).normalise

>>> normalise('Ἀχιλλεύς')
('Ἀχιλλεύς', <Norm.UNCHANGED: 0>)


You can config which normalisations to do:

>>> normalise = Normaliser(config=Norm.GRAVE|Norm.PROCLITIC).normalise

>>> normalise('Τὴν')
('Τήν', <Norm.GRAVE: 1>)

>>> normalise('ὁς')
('ὁς', <Norm.UNCHANGED: 0>)

>>> normalise('μετ’')
('μετ’', <Norm.UNCHANGED: 0>)

>>> normalise('οὐκ')
('οὐκ', <Norm.PROCLITIC: 32>)
