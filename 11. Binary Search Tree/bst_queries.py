# BST Queries
# Asked in companies
# Google
# De Shaw
# Samsung

# Description
# You are given an arbitrary binary search tree (BST) with N nodes numbered from 1 to N. Each node has a value, and you are given Q queries. Each query is of the form [L, R], where L and R are integers representing the range. Your task is to find the number of nodes in the BST whose values lie within the range [L, R] for each query.

# Input:
# root: The root node of the binary search tree (BST).
# queries: A list of Q queries where each query is a list [L, R] representing the range.

# Output:
# A list of integers where each integer represents the count of nodes within the given range for each query.

# Example:

# Input:
# root = [10,5,15,1,7,null,20]
# queries = [[1, 5], [6, 10], [10, 20]]
# Output:
# [2, 1, 2]
# Explanation:
# - For query [1, 5], nodes within the range are [1, 5] (2 nodes).
# - For query [6, 10], nodes within the range are [7, 10] (1 node).
# - For query [10, 20], nodes within the range are [10, 15, 20] (2 nodes).

def count_nodes_in_range_helper(root, L, R):

    if root is None:
        return 0
    
    count = 0

    if L < root.val:
        count = count + count_nodes_in_range_helper(root.left, L, R)

    if L <= root.val and R >= root.val:
        count = count + 1
    
    if R > root.val:
        count = count + count_nodes_in_range_helper(root.right, L, R)

    return count


def count_nodes_in_range(root, queries):
    # Core logic for the learner to implement
    if root is None:
        return []
    
    node_count_lst = []
    for query in queries:
        node_count = count_nodes_in_range_helper(root, query[0], query[1])
        node_count_lst.append(node_count)
    
    return node_count_lst
    