#!/usr/bin/env python3

import sys


if __name__ == "__main__":
    with open("tokens.txt") as f:
        for line in f:
            token = line.strip()
            norm, norm_code = convert(token)
            print(f"{token:20s}\t{norm:20s}\t{'+'.join(norm_code)}")
