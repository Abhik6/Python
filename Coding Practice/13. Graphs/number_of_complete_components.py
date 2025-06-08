# Number of Complete Components
# Asked in Companies:

# Justpay
# Morgan stanley
# Google
# Microsoft


# Description
# You are given an undirected graph with n vertices, numbered from 0 to n - 1. The graph is represented by a 2D integer array edges, where edges[i] = [ai, bi] denotes that there is an undirected edge between vertices ai and bi.
# Your task is to find how many complete connected components the graph contains.
# A connected component is a subgraph where:
# There is a path between any two vertices within the subgraph.
# No vertex in the subgraph shares an edge with a vertex outside of the subgraph.
# A connected component is said to be complete if there is an edge between every pair of vertices in the connected component.


# Input:
# n: An integer representing the number of vertices in the graph.
# edges: A 2D list representing the edges between vertices.

# Output:
# Return the number of complete connected components in the graph.


# Examples:

# Input:
# n = 6
# edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
 
# Output:
# 1
 
# Explanation:
# - The graph has two connected components: 
#   1. {0, 1, 2} which forms a complete connected component.
#   2. {3, 4} which is not complete as there is no edge between node 3 and node 4.
# - Hence, the number of complete connected components is 1.
 
 
# Input:
# n = 4
# edges = [[0, 1], [2, 3]]
 
# Output:
# 0
 
# Explanation:
# - There are two connected components: {0, 1} and {2, 3}, but neither is complete.
# - Hence, the output is 0.

def count_complete_components(n, edges):
    
    # Creating an adjacency list of neighbours
    adj_lst = [[] for _ in range(n)]
    for u, v in edges:
        adj_lst[u].append(v)
        adj_lst[v].append(u) 

    # Get all the connected components in graph  
    visited = []
    components = []
    for node in range(n):
        if node not in visited:
            component = dfs(node, adj_lst, visited, [])
            components.append(component)
    print(components)
    # Check if components are complete. Mark True if complete else False.
    complete_components = 0
    for component in components:
        flag = True
        for node in component:
            if sorted(list(set(component)-set([node]))) != sorted(adj_lst[node]):
                flag = False
                break
        if flag:
            complete_components+=1
    
    return complete_components
    

def dfs(node, adj_lst, visited, component):
    
    component.append(node)
    visited.append(node)

    for neighbour in adj_lst[node]:
        if neighbour not in visited:
            component = dfs(neighbour, adj_lst, visited, component)

    return component


## Another Solution

def count_complete_components(n, edges):
    """
    This function calculates the number of complete connected components in an undirected graph.
    A complete component has an edge between every pair of its vertices.
    """
 
    # Step 1: Create adjacency list
    adj_list = {i: [] for i in range(n)}
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Step 2: Use DFS to find all connected components
    def dfs(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                dfs(neighbor, component)
 
    visited = set()
    components = []
 
    # Step 3: Collect all connected components
    for i in range(n):
        if i not in visited:
            component = []
            dfs(i, component)
            components.append(component)
 
    # Step 4: Check if each component is complete
    def is_complete(component):
        size = len(component)
        expected_edges = (size * (size - 1)) // 2  # Complete graph has n*(n-1)/2 edges
        actual_edges = 0
        
        # Count actual edges in the component
        for node in component:
            actual_edges += len([neighbor for neighbor in adj_list[node] if neighbor in component])
 
        return actual_edges // 2 == expected_edges
 
    # Step 5: Count the number of complete components
    complete_count = 0
    for component in components:
        if is_complete(component):
            complete_count += 1
    
    return complete_count
 
# Explanation:
# 1. We first build the adjacency list from the given edges.
# 2. We use DFS to find all connected components in the graph.
# 3. For each connected component, we check if it forms a complete graph by verifying that the number of edges matches
#    the expected number for a complete graph.
# 4. Finally, we count how many of these connected components are complete.

## Leetcode Solution
class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        # Adjacency lists for each vertex
        graph = [[] for _ in range(n)]
        # Map to store frequency of each unique adjacency list
        component_freq = defaultdict(int)

        # Initialize adjacency lists with self-loops
        for vertex in range(n):
            graph[vertex] = [vertex]

        # Build adjacency lists from edges
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        # Count frequency of each unique adjacency pattern
        for vertex in range(n):
            neighbors = tuple(sorted(graph[vertex]))
            component_freq[neighbors] += 1


# n = 6
# edges = [[0, 1], [0, 2], [1, 2], [3, 4]]

n = 4
edges = [[0, 1], [2, 3]]

print(count_complete_components(n, edges))