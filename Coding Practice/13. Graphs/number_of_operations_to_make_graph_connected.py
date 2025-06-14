# Number of Operations to make Graph Connected
# Description:
# You are given a network of n computers numbered from 0 to n - 1 connected by ethernet cables. Each connection is represented as an edge between two nodes. You can extract certain cables and place them between any pair of disconnected computers to make them directly connected.


# Parameters:
# n (int): The number of computers.
# connections (List[List[int]]): A list of connections where each connection is represented by a pair [ai, bi] indicating a direct connection between computers ai and bi.


# Return Values:
# int: The minimum number of operations required to make all computers connected. If it is not possible, return -1.


# Example:

# Input: n = 5, connections = [[0,1],[1,2],[2,3],[3,4]] 
# Output: 0
# Explanation: All computers are already connected.
 
 
# Input: n = 6, connections = [[0,1],[0,2],[1,2],[3,4]] 
# Output: -1 
# Explanation: It is impossible to connect all computers.

def minOperationsToConnectComputers(n, connections):

    if len(connections)<(n-1):
        return -1
    else:
        adj_lst = [[] for _ in range(n)]
        for u, v in connections:
            adj_lst[u].append(v)
            adj_lst[v].append(u)
        print(adj_lst)
        visited = [False for _ in range(n)]
        num_components = 0

        for node in range(n):
            if not visited[node]:
                dfs(node, visited, adj_lst)
                num_components+=1
                print(num_components)
        
        return num_components-1
    
def dfs(start_node, visited, adj_lst):
    visited[start_node] = True
    print(visited)
    for neighbour in adj_lst[start_node]:
        if not visited[neighbour]:
            dfs(neighbour, visited, adj_lst)

# n = 5
# connections = [[0,1],[1,2],[2,3],[3,4]] 

# n = 6
# connections = [[0,1],[0,2],[1,2],[3,4]] 

# n = 4
# connections = [[0,1],[0,2],[1,2]]

# n = 6
# connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]

n = 6
connections = [[0,1],[0,2],[0,3],[1,2]]

print(minOperationsToConnectComputers(n, connections))