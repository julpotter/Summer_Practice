def list_vertices(g):
    # Your code here
    vertices = []
    for i in g:
        vertices.append(i)
        
    return vertices

print(list_vertices({1:[2, 4], 2:[3, 4], 3:[4], 4:[5], 5:[1]}))
