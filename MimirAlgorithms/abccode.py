import sys


def preceding(p):
    # possible letters preceding
    if p == 'C':
        return ['A', 'C']
    if p == 'B':
        return ['C', 'B']
    if p == 'A':
        return ['A', 'B', 'C']


def childcount(p):
    # possible letters following
    if p == 'C':
        return ['A', 'B', 'C']
    if p == 'B':
        return ['A', 'B']
    if p == 'A':
        return ['A', 'C']


def buildTree(n, tree):

    for v in range(n-1):
        tree.append([])
    for i in range(n-1):
        for j in tree[i]:
            x = childcount(j)
            for k in x:
                tree[i+1].append(k)


def numCodewords(n):
    wordcount = 0
    start = ['C']
    tree = [start]
    buildTree(n+1, tree)
    leaves = tree[-1]
    for i in leaves:
        wordcount += 1

    return wordcount


############### for grading #################


z = int(sys.stdin.readline())
print(numCodewords(z))