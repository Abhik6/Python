# Kth smallest element in BST
# Asked in Companies
# Visa
# Goldman Sachs
# Myntra
# ServiceNow


# Description

# You are given the root of a binary search tree (BST) and an integer k. Your task is to return the k-th smallest value of all the values of the nodes in the tree.

# Input:
# root: The root of the binary search tree (BST).
# k: An integer representing the rank (1-indexed) of the smallest element to find.

# Output:
# Return the k-th smallest value from the BST.



# Example:

# Input:
# root = [3,1,4,null,2], k = 1
# Output:
# 1
# Explanation:
# The in-order traversal of the tree is [1, 2, 3, 4], and the 1st smallest element is 1.
 
 
# Input:
# root = [5,3,6,2,4,null,null,1], k = 3
# Output:
# 3
# Explanation:
# The in-order traversal of the tree is [1, 2, 3, 4, 5, 6], and the 3rd smallest element is 3.

def inorder_BST(root, lst=[]):

    if root is None:
        return []
    
    inorder_BST(root.left, lst)
    lst.append(root.val)
    inorder_BST(root.right, lst)

    return lst

def kth_smallest(root, k):
    # Core logic for the learner to implement
    if root is None:
        return None
    
    inorder_lst = inorder_BST(root, [])

    return inorder_lst[k-1]