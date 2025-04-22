# Recover a BST
# Asked in Companies:

# Microsoft
# Apple
# LinkedIn

# Description:
# You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Your task is to recover the BST by swapping the values of these two nodes back to their correct positions. The structure of the tree should remain unchanged.

# Input Parameters:
# root (TreeNode): The root of the binary search tree.

# Output:
# The root of the corrected binary search tree.

# Example:

# Input:
#       3
#      / \
#     1   4
#        /
#       2
 
# Output:
#       2
#      / \
#     1   4
#        /
#       3
 
# Explanation: The original tree has 2 and 3 swapped. The corrected tree is a valid BST.



def find_min(root):
    if root is None:
        return None
    
    while root.left is not None:
        root = root.left

    return root.val

def find_max(root):
    if root is None:
        return None
    
    while root.right is not None:
        root = root.right

    return root.val

def inorder_BST(root, lst=[]):

    if root is None:
        return []
    
    inorder_BST(root.left, lst)
    lst.append(root.val)
    inorder_BST(root.right, lst)

    return lst

def find_node(root, key):
    if root is None:
        return None
    
    if root.val == key:
        return root
    
    node = find_node(root.left, key)
    if node is None:
        node = find_node(root.right, key)

    return node


def recover_tree(root):
    """
    Function to recover a BST where two nodes were swapped by mistake.
    
    :param root: TreeNode -> The root of the binary search tree
    :return: TreeNode -> The root of the corrected binary search tree
    """

    if root is None:
        return None
    
    inorder_lst = inorder_BST(root, [])
    print(inorder_lst)

    for i in range(len(inorder_lst)):
        if inorder_lst[i] > inorder_lst[i+1]:
            key1, key2 = inorder_lst[i], inorder_lst[i+1]
            break
    print(key1)
    print(key2)
    key1_node = find_node(root, key1)
    key2_node = find_node(root, key2)

    key1_node.val = key2
    key2_node.val = key1

    return root


###### Provided solution #######
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def recover_tree_1(root):
    """
    Function to recover a BST where two nodes were swapped by mistake.
    
    :param root: TreeNode -> The root of the binary search tree
    :return: TreeNode -> The root of the corrected binary search tree
    """
    def inorder_traversal(node):
        if node is None:
            return []
        return inorder_traversal(node.left) + [node] + inorder_traversal(node.right)
    
    # In-order traversal to get nodes in sorted order
    nodes = inorder_traversal(root)
    
    # Find the two nodes that are swapped
    first = second = None
    prev = TreeNode(float('-inf'))
    
    for node in nodes:
        if node.val < prev.val:
            if first is None:
                first = prev
            second = node
        prev = node
    
    # Swap the values of the two nodes
    if first and second:
        first.val, second.val = second.val, first.val
 
    return root
 
# Helper function for debugging (can be removed for production)
def display_recovered_tree(root):
    result = inorder_traversal(root)
    print(result)
 
def inorder_traversal(node):
    """Helper function to get in-order traversal of the tree."""
    if node is None:
        return []
    return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
 
# Example usage (can be removed)
# tree = TreeNode(1)
# tree.left = TreeNode(3)
# tree.right = TreeNode(2)
# recovered_tree = recover_tree(tree)
# print(inorder_traversal(recovered_tree))  # Output: [1, 2, 3]

