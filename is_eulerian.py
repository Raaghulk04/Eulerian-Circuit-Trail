import ast
def is_eulerian_cycle(graph):
    if not is_connected(graph):
        return False
    for node in graph:
        if (len(graph[node]) % 2 != 0):
            return False
    return True    

def is_eulerian_path(graph):
    if not is_connected(graph):
        return False
    odd_degree_count = 0
    for node in graph:
        if (len(graph[node]) % 2 != 0):
            odd_degree_count += 1
    return odd_degree_count == 2

def is_connected(graph):
    """
    Check if an undirected graph is connected.

    Parameters:
    graph (dict): A dictionary representing the adjacency list of the graph.
                  Keys are node identifiers and values are lists of adjacent nodes.

    Returns:
    bool: True if the graph is connected, False otherwise.
    """
    if not graph:
        return True

    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    # Start DFS from the first node in the graph
    start_node = next(iter(graph))
    dfs(start_node)

    # The graph is connected if all nodes were visited
    return len(visited) == len(graph)


graph = ast.literal_eval(input("Enter the graph as an adjacency list (e.g., {0: [1, 2], 1: [0, 2], 2: [0, 1]}): "))
euler_cycle = is_eulerian_cycle(graph)
euler_path = is_eulerian_path(graph)
print(f"Is Eulerian Cycle: {euler_cycle}")
print(f"Is Eulerian Path: {euler_path}")
