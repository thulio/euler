#!/usr/bin/env python3
from problem_4.solution import is_palindrome


def is_double_base_palindrome(number):
    binary_number = str(bin(number)).replace("0b", "")
    return is_palindrome(str(number)) and is_palindrome(binary_number)


if __name__ == "__main__":
    assert is_double_base_palindrome(585)
    print(sum([number for number in range(10 ** 6) if is_double_base_palindrome(number)]))
