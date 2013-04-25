#!/usr/bin/env python3


import itertools

digits = [str(i) for i in range(10)]

permutations = itertools.permutations(digits)

for index, permutation in enumerate(permutations, start=1):
    if index == 10 ** 6:
        print(permutation)
        print("".join(permutation))

print(index)
