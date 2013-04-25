#!/usr/bin/env python3

import math


def check_digits(number, power=4):
    sum_ = sum([math.pow(int(i), power) for i in str(number)])

    return sum_ == number


if __name__ == "__main__":
    assert check_digits(1634)
    numbers = []
    for i in range(2, 10 ** 6):
        if check_digits(i, 5):
            numbers.append(i)

    print(sum(numbers))
