# Count elements in all subtrees
# Asked in Companies:

# Cisco
# Samsung
# Thought works


# Description:
# You are given an arbitrary tree consisting of 'N' nodes numbered from 0 to N-1. You need to find the total number of elements in all the subtrees of the given tree. In other words, for each node in the tree, you are required to return the count of nodes in the subtree rooted at that node.
# A subtree of a tree T is a tree S consisting of a node in T and all of its descendants in T. The subtree corresponding to the root node is the entire tree.
# The tree is represented using an array of edges where each edge connects two nodes in the tree.


# Input:
# n (integer): The number of nodes in the tree.
# edges (List[List[int]]): A 2D list of edges, where edges[i] = [u, v] represents an edge between nodes u and v.

# Output:
# Return a list of integers where the i-th element is the number of nodes in the subtree rooted at node i.


# Examples:

# Input: 
# n = 6
# edges = [[0,1],[0,2],[1,3],[1,4],[2,5]]
# Output: [6, 3, 2, 1, 1, 1]
# Explanation: 
# Node 0 is the root and has 5 other nodes in its subtree.
# Node 1 has 3 nodes (including itself).
# Node 2 has 2 nodes (including itself).
# Nodes 3, 4, and 5 are leaves and have 1 node each (themselves).
 
# Input: 
# n = 5
# edges = [[0,1],[0,2],[2,3],[2,4]]
# Output: [5, 1, 3, 1, 1]
# Explanation:
# Node 0 has 5 nodes in total (entire tree).
# Node 1 is a leaf and has only itself.
# Node 2 has 3 nodes in its subtree.
# Nodes 3 and 4 are leaves with 1 node each.


def countSubtreeNodes(n, edges):
    # To be implemented
    adj_lst = [[] for i in range(n)]
    for u, v in edges:
        adj_lst[u].append(v)
    
    print(adj_lst)

    subtree_nodes = [0 for i in range(n)]
    for node in range(n):
        count = dfs(node, adj_lst, 0)
        subtree_nodes[node] = count

    return subtree_nodes

def dfs(node, adj_lst, count=0):
    
    count = 1
    for neighbour in adj_lst[node]:
        count+=dfs(neighbour, adj_lst)
    
    return count

# n = 6
# edges = [[0,1],[0,2],[1,3],[1,4],[2,5]]

n = 5
edges = [[0,1],[0,2],[2,3],[2,4]]

print(countSubtreeNodes(n, edges))

