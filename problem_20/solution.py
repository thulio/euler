#!/usr/bin/env python
import functools

from problem_16.solution import sum_of_digits


def factorial(number):
    numbers = []
    while number > 1:
        numbers.append(number)
        number -= 1

    return functools.reduce(lambda x, y: x * y, numbers)


if __name__ == "__main__":
    assert 3628800 == factorial(10)
    factorial_of_100 = factorial(100)
    print(sum_of_digits(factorial_of_100))