# Reverse all arcs in a digraph (or graph)
def graph_reverse(g):
    N = len(g)
    l = {}
    for p in range(N):
        l[p] = []

    print(g)
    for i in g:
        print(i)
        for j in g[i]:
            print("j is " + str(j))
            print("g[j] is " + str(g[j]))
            if i not in l[j]:
                l[j].append(i)
    return l
g = {0: [1, 3], 1: [4, 2], 2: [4], 3: [1], 4: [3, 1]}
#{0: [1, 2], 1: [0], 2: [0]}
#{1:[2, 4], 2:[3, 4], 3:[4], 4:[5], 5:[1]}
print(graph_reverse(g))