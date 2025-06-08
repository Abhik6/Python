# Number of Unreachable Nodes
# Asken in Companies:

# Directi

# Amazon

# Synopsys



# Description:

# You are given an undirected graph with n nodes, numbered from 0 to n - 1. The graph is represented by a 2D integer array edges, where edges[i] = [ai, bi] denotes an undirected edge between the nodes ai and bi.

# Your task is to return the number of pairs of different nodes that are unreachable from each other. A pair (i, j) is considered unreachable if there is no path from node i to node j.



# Input:

# n: An integer representing the number of nodes.

# edges: A 2D list of integer pairs representing the edges between nodes.

# Output:

# Return the number of unreachable pairs of nodes.



# Example:

# Input:
# n = 5
# edges = [[0, 1], [0, 2], [3, 4]]
 
# Output:
# 6
 
# Explanation:
# - The graph has two connected components: {0, 1, 2} and {3, 4}.
# - Unreachable pairs are: (0, 3), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4).
# - Hence, the output is 6.
 
 
# Input:
# n = 7
# edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]
 
# Output:
# 14
 
# Explanation:
# - The graph has two connected components: {0, 2, 4, 5} and {1, 6}.
# - Unreachable pairs are: (0, 1), (0, 6), (2, 1), (2, 6), (4, 1), (4, 6), (5, 1), (5, 6).
# - Hence, the output is 14.

def count_unreachable_pairs(n, edges):
    # Core logic for the learner to implement
    
    components = []
    visited = []
    for node in range(n):
        if node not in visited:
            component = traverse_dfs(node, n, edges, visited, [])
            components.append(component)

    count = 0
    for source_index in range(len(components)):
        for destination_index in range(source_index+1,len(components)):
            count+=len(components[source_index])*len(components[destination_index])

    return count

def traverse_dfs(start_index, n, edges, visited=[], component=[]):
    visited.append(start_index)
    component.append(start_index)
    print(component)
    for neighbour in range(start_index+1, n):
        if [start_index, neighbour] in edges or [neighbour, start_index] in edges:
            if neighbour not in visited:
                component = traverse_dfs(neighbour, n, edges, visited, component)

    return component


class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        # Core logic for the learner to implement
        # Step 1: Create an adjacency list for the grap
        adj_lst = {i: [] for i in range(n)}
        for u, v in edges:
            adj_lst[u].append(v)
            adj_lst[v].append(u)

        # Step 2: Perform DFS to find all connected components
        components = []
        visited = []
        for node in range(n):
            if node not in visited:
                component = self.traverse_dfs(node, n, adj_lst, visited, [])
                components.append(len(component))

        # count = 0
        # for source_index in range(len(components)):
        #     for destination_index in range(source_index+1,len(components)):
        #         count+=len(components[source_index])*len(components[destination_index])

        # Step 3: Calculate the total number of possible pairs (n choose 2)
        total_pairs = n*(n-1)//2

        # Step 4: Calculate the number of reachable pairs within each component
        reachable_pairs = 0
        for size in components:
            reachable_pairs+= size*(size-1)//2

        unreachable_pairs = total_pairs - reachable_pairs

        return unreachable_pairs

    def traverse_dfs(self, start_index, n, adj_lst, visited=[], component=[]):
        visited.append(start_index)
        component.append(start_index)
        print(component)
        neighbours = adj_lst[start_index]
        for neighbour in neighbours:
            if neighbour not in visited:
                component = self.traverse_dfs(neighbour, n, adj_lst, visited, component)

        return component


n = 7
edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
print(count_unreachable_pairs(n, edges))
