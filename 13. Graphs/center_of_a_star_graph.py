# Center of a Star Graph
# Asked in Companies:

# Cisco
# Microsoft
# Sprinklr


# Description:
# A star graph is a graph consisting of n nodes, labeled from 1 to n. It has one center node connected to exactly n-1 other nodes, forming n-1 edges. The goal is to find the center node of the star graph.
# You are given a 2D integer array edges where edges[i] = [ui, vi] represents an edge between node ui and node vi. Your task is to return the node that is the center of the star graph.

# Input Parameters:
# edges (List[List[int]]): A list of edges, where each edge connects two nodes.

# Output:
# Return the center node of the star graph.


# Example:

# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
# Explanation: As node 2 is connected to all other nodes, it is the center of the star graph.
 
# Input: edges = [[1,3],[3,4],[3,2]]
# Output: 3


def find_center(edges):
    """
    Function to find the center node of the star graph.
    
    :param edges: List[List[int]] -> List of edges connecting the nodes
    :return: int -> The center node
    """
    # TODO: Implement the logic to find the center node
    
    vertices = []
    for u, v in edges:
        if u not in vertices:
            vertices.append(u)
        if v not in vertices:
            vertices.append(v)

    n = len(vertices)
    print(n)
    adj_lst = {i: [] for i in range(1, n+1)}
    for node in range(1, n+1):
        adj_lst[node].append(node)
    print(adj_lst)
    for u, v in edges:
        adj_lst[u].append(v)
        adj_lst[v].append(u)
    
    print(adj_lst)
    for node, neighbours in adj_lst.items():
        if len(neighbours) == n:
            return node

# edges = [[1,2],[2,3],[4,2]]
edges =  [[1,3],[3,4],[3,2]]
print(find_center(edges))
