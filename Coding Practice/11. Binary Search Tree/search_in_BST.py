# Search in a BST
# Asked in Companies:

# Google
# Amazon
# Facebook
# Microsoft

# Description:
# You are given the root of a binary search tree (BST) and an integer val. Your task is to find the node in the BST whose value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

# A binary search tree (BST) is a binary tree in which for every node, all elements in the left subtree are smaller, and all elements in the right subtree are larger than the node's value.

# Input Parameters:
# root (TreeNode): The root node of the binary search tree.
# val (int): The value to search for in the tree.

# Output:
# The node whose value matches val, or None if the node does not exist in the tree.

# Example:

# Input:
#         4
#        / \
#       2   7
#      / \
#     1   3
# val = 2
 
# Output:
#       2
#      / \
#     1   3
 
 
# Input: 
#         4
#        / \
#       2   7
#      / \
#     1   3
# val = 5
 
# Output: None

from common import BSTNode

def search_bst(root, val):
    """
    Function to search for a node in a Binary Search Tree (BST) whose value equals val.
    :param root: TreeNode -> root of the binary search tree
    :param val: int -> the value to search for
    :return: TreeNode -> the node whose value equals val, or None if it doesn't exist
    """

    if root is None:
        return None
    
    if root.val == val:
        return root
    
    if val < root.val:
        root = search_bst(root.left, val)
    else:
        root = search_bst(root.right, val)

    return root

