#!/usr/bin/env python


def gen_primes(number):
    """
    http://stackoverflow.com/a/568618
    """
    composites = {}
    prime = 2

    while prime < number:
        if prime not in composites:
            yield prime

            composites[prime * prime] = [prime]
        else:
            for p in composites[prime]:
                composites.setdefault(p + prime, []).append(p)

            del composites[prime]

        prime += 1


if __name__ == "__main__":
    number = 600851475143
    factors = []
    primes = list(gen_primes(number ** 0.5))
    for factor in primes:
        if number % factor == 0:
            factors.append(factor)

    print(max(factors))
