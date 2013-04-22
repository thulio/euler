#!/usr/bin/env python


def fibonnaci(number):
    assert number > 0
    a, b = 0, 1
    for i in range(number):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    number = 1
    numbers = []
    fibo = fibonnaci(9999)

    while True:
        i = next(fibo)
        if i < 4 * 10 ** 6:
            if (i % 2 == 0):
                numbers.append(i)
        else:
            break

    print(sum(numbers))
