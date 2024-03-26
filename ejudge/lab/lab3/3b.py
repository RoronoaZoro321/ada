def dfs(graph, node, visited, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    stack.append(node)


def dfs_reverse(graph, node, visited, scc):
    visited[node] = True
    scc.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_reverse(graph, neighbor, visited, scc)


def kosaraju(graph, reverse_graph, nodes):
    visited = {node: False for node in nodes}
    stack = []

    # First DFS to fill the stack
    for node in nodes:
        if not visited[node]:
            dfs(graph, node, visited, stack)

    # Second DFS in reverse order
    visited = {node: False for node in nodes}
    sccs = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            scc = []
            dfs_reverse(reverse_graph, node, visited, scc)
            sccs.append(sorted(scc))
    return sorted(sccs)


def main():
    number = int(input())
    if number == 0:
        print("No nodes in the graph")
        return

    graph = {}
    reverse_graph = {}
    nodes = set()

    while True:
        node_u, node_v = map(int, input().split())
        if node_u == 0 and node_v == 0:
            break
        if node_u not in graph:
            graph[node_u] = []
        if node_v not in graph:
            graph[node_v] = []
        if node_v not in reverse_graph:
            reverse_graph[node_v] = []
        if node_u not in reverse_graph:
            reverse_graph[node_u] = []
        graph[node_u].append(node_v)
        reverse_graph[node_v].append(node_u)
        nodes.add(node_u)
        nodes.add(node_v)

    sccs = kosaraju(graph, reverse_graph, nodes)

    for scc in sccs:
        print(" ".join(map(str, scc)))


if __name__ == "__main__":
    main()
