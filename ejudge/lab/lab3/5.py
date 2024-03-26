import math

def euclidean_distance(city1, city2):
    x_1, y_1 = city1
    x_2, y_2 = city2
    return math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

def prim(graph):
    visited = {0}
    min_cost = 0
    while len(visited) < len(graph):
        min_edge = float("inf")
        min_node = None
        for node in visited:
            for neighbor, cost in graph[node].items():
                if neighbor not in visited and cost < min_edge:
                    min_edge = cost
                    min_node = neighbor
        visited.add(min_node)
        min_cost += min_edge
    return min_cost

def minimum_budget(amount, cities):
    graph = {i: {} for i in range(amount)}
    for i in range(amount):
        for j in range(i + 1, amount):
            distance = euclidean_distance(cities[i], cities[j])
            graph[i][j] = distance
            graph[j][i] = distance
    return round(prim(graph), 2)

def main():
    amount = int(input())
    cities = [tuple(map(int, input().split())) for _ in range(amount)]
    print(minimum_budget(amount, cities))

if __name__ == "__main__":
    main()