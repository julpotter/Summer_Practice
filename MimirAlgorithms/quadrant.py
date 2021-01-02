import sys


def quadrant(x, y):
    if x < 0:
        if y < 0:
            return 3
        if y > 0:
            return 2
    if x > 0:
        if y < 0:
            return 4
        if y > 0:
            return 1


for i in sys.stdin:
    ab = i.split()
    a = int(ab[0])
    b = int(ab[1])

    res = quadrant(a, b)
    print(res)
