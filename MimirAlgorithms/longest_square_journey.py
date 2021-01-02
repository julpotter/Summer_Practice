import math
L = [1, 5, 18, 32, 46, 53, 54, 62, 70, 85, 97, 99, 111, 116, 126, 133, 140, 145, 148, 151]


def longest_square_paths(L):
    longest_paths = [[]]
    if not L[:-1]:
        return [[L[-1]]]
    else:
        lsp = longest_square_paths(L[:-1])
        for i in lsp:
            if math.sqrt(L[-1] - i[-1]) % 1 == 0.0:
                longest_paths = []
                longest_paths.append(i + [L[-1]])
        if longest_paths[0]:
            return lsp + longest_paths
        else:
            return lsp


def longest_square_journey(L):
    longest_journey = []
    for i in longest_square_paths(L):
        if len(i) > len(longest_journey):
            longest_journey = i

    return len(longest_journey) - 1