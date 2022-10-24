graph = {
    'S': [('A', 1), ('B', 2)],
    'A': [('Y', 7), ('X', 4)],
    'B': [('C', 7), ('D', 1)],
    'Y': [('E', 3)],
    'X': [('E', 4)],
    'C': [('E', 5)],
    'D': [('E', 12)]
}

h = {
    'S': 20,
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 15,
    'X': 5,
    'Y': 8,
    'E': 0
}

def Gready_best_search(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)


solution = Gready_best_search(graph, 'S', 'E')
print('Path: ', solution)
