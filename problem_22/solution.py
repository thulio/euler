#!/usr/bin/env python
import functools
import os.path

PROBLEM_ROOT = os.path.abspath(os.path.dirname(__file__))


def name_score(name, position):
    name_sum = functools.reduce(lambda x, y: x + y, [ord(c.lower()) - 96 for c in name])
    return name_sum * position


if __name__ == "__main__":
    assert 49714 == name_score("COLIN", 938)
    total = 0
    with open(os.path.join(PROBLEM_ROOT, "names.txt")) as f:
        file_content = f.read()
        names = file_content.replace('"', "").split(",")
        names = sorted(names)
        for index, name in enumerate(names, start=1):
            total += name_score(name, index)

    print(total)