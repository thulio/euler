#!/usr/bin/env python
from problem_3.solution_3 import gen_primes

PRIMES = list(gen_primes(1000000))


if __name__ == "__main__":
    print(PRIMES[10000])
