from collections import defaultdict
from typing import List

def directed_dfs(graph: defaultdict, rec_stack: set, visited: set, cycle: List[int], node: int) -> bool:
        visited.add(node)
        rec_stack.add(node)
        cycle.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(graph, rec_stack, visited, cycle, neighbor):
                    return True
            elif neighbor in rec_stack:
                cycle.append(neighbor)
                return True
        
        rec_stack.remove(node)
        cycle.pop()
        return False

def dfs(node, parent, graph, visited, cycle):
    visited.add(node)
    cycle.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(neighbor, node, graph, visited, cycle):
                return True
        elif neighbor != parent:
            # Cycle detected
            cycle.append(neighbor)
            return True

    cycle.pop()
    return False

def find_cycle(num_nodes, edges):
    graph = {i: [] for i in range(num_nodes)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    cycle = []

    for i in range(num_nodes):
        if i not in visited:
            if dfs(i, -1, graph, visited, cycle):
                return cycle  # Return the cycle in the correct order

    return []  # No cycle found

# Example usage
num_nodes = 5
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 1)]

cycle = find_cycle(num_nodes, edges)
if cycle:
    print("Cycle detected:", cycle)
else:
    print("No cycle detected.")
