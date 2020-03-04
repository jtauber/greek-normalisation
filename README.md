# greek-normalisation

[![Build Status](https://travis-ci.org/jtauber/greek-normalisation.svg)](https://travis-ci.org/jtauber/greek-normalisation)
[![Coverage Status](https://coveralls.io/repos/github/jtauber/greek-normalisation/badge.svg?branch=master)](https://coveralls.io/github/jtauber/greek-normalisation?branch=master)

utilities for validating and normalising Ancient Greek text

For more of my work on Ancient Greek, see <http://jktauber.com/>.

## Installation

```
pip install greek-normalisation
```

## Documentation / Tests

See `tests.rst` for usage examples.

Also, three command-line utilities `to2019`, `toNFC` and `toNFD` are installed which can be used to convert U+02BC and U+1FBF to U+2019 and do unicode normalisation on files (e.g. `toNFC source.txt > nfc_version.txt`).
