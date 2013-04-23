#!/usr/bin/env python
import math


def make_powers(max_power):
    powers = set()

    for i in range(2, max_power + 1):
        for j in range(2, max_power + 1):
            powers.add(math.pow(i, j))

    return powers

if __name__ == "__main__":
    assert 15 == len(make_powers(5))
    print(len(make_powers(100)))
