#!/usr/bin/env python
import functools


def sum_of_squares(number):
    return functools.reduce(lambda x, y: x + y, [x ** 2 for x in range(1, number + 1)])


def square_of_sums(number):
    return functools.reduce(lambda x, y: x + y, range(1, number + 1)) ** 2


if __name__ == "__main__":
    s1 = (sum_of_squares(100))
    s2 = (square_of_sums(100))
    print(s2 - s1)
