# Successor and Predecessor in a BST
# Asked in Companies:
# De Shaw
# IBM
# Oracle

# Description:
# You are given a binary search tree (BST) with N nodes and an integer KEY representing the data of a node in this BST. Your task is to find and return the predecessor and successor of the node with the given KEY.

# Predecessor: The node that would be visited immediately before the node with KEY in an inorder traversal of the BST. If the given node is the first node in the inorder traversal, the predecessor should be NULL.

# Successor: The node that would be visited immediately after the node with KEY in an inorder traversal of the BST. If the given node is the last node in the inorder traversal, the successor should be NULL.

# Input Parameters:
# root (TreeNode): The root of the binary search tree.
# KEY (int): The data value of the node for which to find the predecessor and successor.

# Output:
# A tuple (predecessor, successor), where both predecessor and successor are integers. If the predecessor or successor does not exist, return None for that value.

# Example:

# Input:
#       20
#      /  \
#     10   30
#    / \    \
#   5  15   35
# KEY = 35
# Output: (30, None)
# Explanation: In the inorder traversal [5, 10, 15, 20, 30, 35], the predecessor of 35 is 30 and there is no successor.
 
 
# Input:
#       20
#      /  \
#     10   30
#    / \    \
#   5  15   35
# KEY = 10
# Output: (5, 15)
# Explanation: In the inorder traversal [5, 10, 15, 20, 30, 35], the predecessor of 10 is 5 and the successor is 15.


def inorder_BST(root, lst=[]):
    if root is None:
        return []
    
    inorder_BST(root.left, lst)
    lst.append(root.val)
    inorder_BST(root.right, lst)

    return lst

def find_predecessor_successor(root, key):
    """
    Function to find the predecessor and successor of a node with the given key in a BST.
    
    :param root: TreeNode -> The root of the binary search tree
    :param key: int -> The value of the node for which to find the predecessor and successor
    :return: Tuple[Optional[int], Optional[int]] -> A tuple containing the predecessor and successor
    """

    if root is None:
        return None, None
    
    inorder_lst = inorder_BST(root, [])

    for i in range(len(inorder_lst)):    
        if key == inorder_lst[i]:
            if i == len(inorder_lst) - 1:
                predecessor = inorder_lst[i-1]
                successor = None
            elif i == 1:
                predecessor = None
                successor = inorder_lst[i+1]
            else:
                predecessor = inorder_lst[i-1]
                successor = inorder_lst[i+1]
        

    return predecessor, successor