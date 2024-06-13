graph = {
    'A': {'B': 260, 'C': 270},
    'B': {'D': 185, 'C': 302, 'E': 363},
    'C': {'E': 243},
    'D': {'F': 272, 'E': 321},
    'E': {'F': 150},
    'F': {}
}

def greedy_shortest_path(graph, start, end):
    current_node = start
    path = [current_node]
    total_distance = 0

    while current_node != end:
        neighbors = graph[current_node]
        if not neighbors:
            break
        next_node = min(neighbors, key=neighbors.get)
        total_distance += neighbors[next_node]
        current_node = next_node
        path.append(current_node)

    return path, total_distance

path, distance = greedy_shortest_path(graph, 'A', 'F')
print(f"Jalur terdekat: {' -> '.join(path)}")
print(f"Total jarak: {distance} meter")