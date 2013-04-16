#!/usr/bin/env python

from problem_3.solution_3 import gen_primes


def is_palindrome(str_number):
    return str_number == "".join(reversed(str_number))


if __name__ == "__main__":
    palindromes = []
    primes = list(gen_primes(998001))
    for i in range(100000, 998001):
        if is_palindrome(str(i)) and i not in primes:
            palindromes.append(i)

    print(max(palindromes))
