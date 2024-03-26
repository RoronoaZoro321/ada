from collections import defaultdict, deque

def build_graph(words):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Initialize in-degree for each character
    for word in words:
        for char in word:
            in_degree[char] = 0
    
    # Build graph and update in-degrees
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))
        for j in range(min_len):
            if word1[j] != word2[j]:
                graph[word1[j]].append(word2[j])
                in_degree[word2[j]] += 1
                break
        else:
            if len(word1) > len(word2):
                return None, None  # Invalid input
    
    return graph, in_degree

def topological_sort(graph, in_degree):
    result = []
    queue = deque()
    
    # Add characters with in-degree 0 to the queue
    for char in in_degree:
        if in_degree[char] == 0:
            queue.append(char)
    
    while queue:
        if len(queue) > 1:  # Multiple options
            queue = deque(sorted(queue))  # Sort to respect English alphabet order
        char = queue.popleft()
        result.append(char)
        
        for adj_char in graph[char]:
            in_degree[adj_char] -= 1
            if in_degree[adj_char] == 0:
                queue.append(adj_char)
    
    if len(result) != len(in_degree):
        return None  # Cycle detected
    
    return ''.join(result)

def strange_alphabet(words):
    graph, in_degree = build_graph(words)
    if graph is None:
        return "INVALID INPUT"
    
    result = topological_sort(graph, in_degree)
    if result is None:
        return "INVALID INPUT"
    
    return result

# Process inputs until '#' is encountered
inputs = []
while True:
    line = input().strip()
    if line == "#":
        break
    inputs.append(line)

# Call the function for each set of inputs and print the result
print(strange_alphabet(inputs))