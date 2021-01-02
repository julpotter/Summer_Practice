def halfway_point(g, start, end):
    for i in g[start]:
        if end in g[i]:
            return True
        else:
            continue
    return False


def num_triangles(g):
    triangles = 0
    trianglepoints = []
    for i in g:
        print("\ni is " + str(i))
        for j in g[i]:
            print("j is " + str(j))
            for h in g[j]:
                if h==i:
                    continue
                for p in g[h]:
                    print("h is " + str(h))
                    print("p is " + str(p))
                    if p==i:
                        N = len(trianglepoints)
                        alreadyTriangle = False
                        for k in range(N):
                            print("Testing through trianglepoints")

                            if h in trianglepoints[k] and j in trianglepoints[k] and i in trianglepoints[k]:
                                print("This triangle is already in trianglepoints")
                                alreadyTriangle = True
                                break

                        if alreadyTriangle == False:
                            triangles += 1
                            print(triangles)
                            trianglepoints.append([i, j, h])
                            print(trianglepoints)


                        # if h not in trianglepoints or j not in trianglepoints or i not in trianglepoints:
                        #     triangles+=1
                        #     print(triangles)
                        #     trianglepoints.append([i,j,h])
                        #     print(trianglepoints)

    return triangles

g = {0: [1,3,5], 1: [0,4,6,5,2], 2: [5,3,1], 3: [2,4,5,0], 4: [3,2,1], 5: [6,1,0,2], 6: [1,5]}
#{0: [1,3,5], 1: [0,4,6,5,2], 2: [5,3,1], 3: [2,4,5,0], 4: [3,2,1], 5: [6,1,0,2], 6: [1,5]}
#{0: [1, 2, 3], 1: [0, 2, 4], 2: [0, 1, 5], 3: [0, 4, 5], 4: [1, 3, 5], 5: [2, 3, 4]}
print(num_triangles(g))

    # triangles = 0
    # start = 0
    # end = 0
    # for i in g:
    #     for j in g:
    #         start = i
    #         end = j
    #         if halfway_point(g, start, end):
    #             if start in g[end] or end in g[start]:
    #                 triangles += 1