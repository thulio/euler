#!/usr/bin/env python


def is_pythagorean_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


if __name__ == "__main__":
    assert is_pythagorean_triplet(3, 4, 5)
    already_tested = {}
    try:
        for a in range(2, 1000):
            if a not in already_tested:
                for b in range(2, 1000):
                    for c in range(2, 1000):
                        if a + b + c != 1000:
                            continue
                        if is_pythagorean_triplet(a, b, c):
                            print("{} {} {} {}".format(a, b, c, (a + b + c)))
                            raise StopIteration
    except:
        print("{} {} {} {}".format(a, b, c, (a * b * c)))
