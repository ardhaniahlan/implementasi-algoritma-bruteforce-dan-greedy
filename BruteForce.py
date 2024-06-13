from itertools import permutations

# Definisikan jarak antar node
distances = {
    ('A', 'B'): 260,
    ('A', 'C'): 270,
    ('B', 'D'): 185,
    ('B', 'C'): 302,
    ('B', 'E'): 363,
    ('C', 'E'): 243,
    ('D', 'F'): 272,
    ('D', 'E'): 321,
    ('E', 'F'): 150
}

def calculate_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        if (route[i], route[i+1]) in distances:
            total_distance += distances[(route[i], route[i+1])]
        elif (route[i+1], route[i]) in distances:
            total_distance += distances[(route[i+1], route[i])]
        else:
            return float('inf')
    return total_distance

nodes = ['A', 'B', 'C', 'D', 'E', 'F']

all_routes = permutations(nodes)

valid_routes = [route for route in all_routes if route[0] == 'A' and route[-1] == 'F']

for route in valid_routes:
    distance = calculate_distance(route)
    if distance < float('inf'):
        print(f"Rute: {' -> '.join(route)}, Jarak: {distance}m")