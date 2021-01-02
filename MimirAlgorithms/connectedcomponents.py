# Returns the number of connected components of
# a graph g. Connected graphs will return "1"


def num_parts(g):
    visited = []
    unvisited = []
    stack = []
    components = 1

    for j in g:
        if j not in unvisited:
            unvisited.append(j)
        for k in g[j]:
            if k not in unvisited:
                unvisited.append(k)
                #print(unvisited)

    for i in g:
        start = i
        break

    stack.append(start)
    visited.append(start)
    if start in unvisited:
        unvisited.remove(start)

    while stack:
        #print("The stack before the pop is " + str(stack))
        x = stack.pop()
        #print("We popped off " + str(x))
        #print("The stack is now " + str(stack))
        #print("We've visited " + str(visited))
        if not g[x]:
            components += 1

        for i in g[x]:
            if i not in visited:
                print(stack)
                visited.append(i)
                stack.append(i)
                print("The stack is now " + str(stack))
                print(stack)
                print(visited)

                if i in unvisited:
                    unvisited.remove(i)
                #print("The unvisited points are " + str(unvisited))
                #print("The stack is " + str(stack))

            if not stack and unvisited:
                components += 1
                print("The number of components is " + str(components))
                new_start = unvisited[0]
                stack.append(new_start)
                unvisited.remove(new_start)

    return components


g = {0: [5, 1, 2], 1: [2, 4, 5, 0], 2: [1, 0, 3], 3: [2], 4: [1], 5: [0, 1], 6: [7, 9], 7: [6], 9: [6], 10: [11, 12], 11: [10], 12: [10]}
#3 components

#{0: [2], 1: [5], 2: [0, 4], 3: [], 4: [2], 5: [1]}
print(num_parts(g))
