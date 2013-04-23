#!/usr/bin/env python
from decimal import Decimal
import functools
import math


def sum_of_digits(number):
    list_of_digits = [int(digit) for digit in str(Decimal(number))]
    return functools.reduce(lambda x, y: x + y, list_of_digits)


if __name__ == "__main__":
    print(sum_of_digits(2**15))
    assert 26 == sum_of_digits(2**15)
    number = Decimal(math.pow(2, 1000))
    print("{}".format(sum_of_digits(number)))