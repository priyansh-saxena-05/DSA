from collections import deque, defaultdict

def topological_sort_bfs(num_vertices, edges):
    # Step 1: Build the adjacency list and in-degree array
    graph = defaultdict(list)
    in_degree = [0] * num_vertices

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Step 2: Add nodes with in-degree 0 to the queue
    queue = deque([i for i in range(num_vertices) if in_degree[i] == 0])
    topo_order = []

    # Step 3: Process nodes in the queue
    while queue:
        current = queue.popleft()
        topo_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If topological ordering includes all nodes, return it; otherwise, there's a cycle
    if len(topo_order) == num_vertices:
        return topo_order
    else:
        return []  # Graph contains a cycle


# Example Usage
vertices = 6
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
print(topological_sort_bfs(vertices, edges))  # Output: [5, 4, 2, 3, 1, 0]



from collections import defaultdict

def topological_sort_dfs(num_vertices, edges):
    # Step 1: Build the adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = [False] * num_vertices
    stack = []

    # Step 2: Define the DFS helper function
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)  # Add the node to the stack after visiting all neighbors

    # Step 3: Perform DFS for all unvisited nodes
    for i in range(num_vertices):
        if not visited[i]:
            dfs(i)

    # Return the reverse of the stack
    return stack[::-1]


# Example Usage
vertices = 6
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
print(topological_sort_dfs(vertices, edges))  # Output: [5, 4, 2, 3, 1, 0]