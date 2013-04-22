#!/usr/bin/env python3


def factorize(number):
    factors = []
    factor = 1
    while factor <= (number / 2):
        if number % factor == 0:
            factors.append(factor)

        factor += 1

    factors.append(number)
    return factors


def num_factors(number):
    factor = 1
    count = 0
    while factor <= (number ** 0.5):
        if number % factor == 0:
            count += 2

        factor += 1

    return count


def gen_triangle_numbers():
    _sum = 0
    _next = 1
    while True:
        _sum += _next
        _next += 1
        yield _sum


if __name__ == "__main__":
    generator = gen_triangle_numbers()
    first_seven_numbers = [1, 3, 6, 10, 15, 21, 28]
    factors_of_3 = [1, 3]
    factors_of_21 = [1, 3, 7, 21]
    assert num_factors(21) == 4
    assert num_factors(3) == 2
    assert factorize(3) == factors_of_3
    assert factorize(21) == factors_of_21
    assert [next(generator) for i in range(7)] == first_seven_numbers

    while True:
        number = next(generator)
        factors = num_factors(number)
        if factors > 300:
            print("{} {}".format(number, factors))
        if factors >= 500:
            print("{} {}".format(number, factors))
            break
