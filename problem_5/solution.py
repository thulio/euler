#!/usr/bin/env python


def is_divisible(number, factors):
    return all([number % factor == 0 for factor in factors])

if __name__ == "__main__":
    from functools import reduce
    primes = [2 ** 4, 3 ** 2, 5, 7, 11, 13, 17, 19]
    number = reduce(lambda x, y: x * y, primes)
    assert is_divisible(number, range(1, 21))
    print(number)
