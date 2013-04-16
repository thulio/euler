#!/usr/bin/env python


def is_n_multiple(base, number):
    return (number % base) == 0


if __name__ == "__main__":
    numbers = []
    for number in range(1000):
        if is_n_multiple(3, number) or is_n_multiple(5, number):
            numbers.append(number)

    print(sum(numbers))
