#!/usr/bin/env python
from problem_3.solution_3 import gen_primes

PRIMES = [prime for prime in gen_primes(2 * 10 ** 6) if prime < 2 * 10 ** 6]


if __name__ == "__main__":
    import functools
    print("{}".format(functools.reduce(lambda x, y: x + y, PRIMES)))
