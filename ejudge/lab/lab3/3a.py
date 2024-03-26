def dfs(graph, visited, node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)

def find_critical_nodes(graph, N):
    critical_nodes = []
    for node in range(1, N+1):
        visited = [False] * (N+1)
        visited[node] = True
        if node > 1:
            visited[1] = False
        components = 0
        for i in range(1, N+1):
            if not visited[i]:
                dfs(graph, visited, i)
                components += 1
        if components > 1:
            critical_nodes.append(node)
    return critical_nodes

def main():
    N = int(input())
    graph = {}
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    critical_nodes = find_critical_nodes(graph, N)
    print(' '.join(map(str, sorted(critical_nodes))))

if __name__ == "__main__":
    main()