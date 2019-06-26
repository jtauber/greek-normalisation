# Tests

    This is a literate doctest.
    Run ``python3 -m doctest -v tests.rst`` to test.

## greek_normalisation.utils

>>> from greek_normalisation.utils import (
...     strip_accents, count_accents, strip_last_accent, grave_to_acute,
...     strip_last_accent_if_two, breathing_check
... )

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