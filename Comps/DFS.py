from typing import Set, Dict, List


def dfs_visit(vertex: int, visited: Set[int], graph: Dict[int, List[int]]):
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            visited.add(neighbor)
            dfs_visit(neighbor, visited, graph)


def dfs(graph: Dict[int, List[int]]):
    visited = set()
    for vertex in graph.keys():
        if vertex not in visited:
            dfs_visit(vertex, visited, graph)


g = {0: [5, 1, 2], 1: [2, 4, 5, 0], 2: [1, 0, 3], 3: [2], 4: [1], 5: [0, 1], 6: [7, 9], 7: [6], 9: [6], 10: [11, 12], 11: [10], 12: [10]}

print(dfs(g))

# runtime is theta(V + E) since dfs() function iterates over all vertices and
# dfs_visit() function iterates over all edges
