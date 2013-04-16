#!/usr/bin/env python


def is_palindrome(str_number):
    return str_number == "".join(reversed(str_number))


if __name__ == "__main__":
    palindrome = 0
    max_factor = 999
    min_factor = 100

    while min_factor <= max_factor:
        mult = min_factor * max_factor
        if is_palindrome(str(mult)) and mult > palindrome:
            palindrome = mult

        min_factor += 1
        if min_factor == max_factor:
            min_factor = 100
            max_factor -= 1

    print(palindrome)
