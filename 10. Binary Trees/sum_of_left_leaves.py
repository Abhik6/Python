from common import *

def is_leaf_node(root):

    if root is None:
        return False
    
    if root.left is None and root.right is None:
        return True
    
    return False


def sum_of_left_leaves_helper(root, sum=0):
    """
    Function to find the sum of all left leaves in a binary tree.
    :param root: TreeNode -> The root of the binary tree
    :return: int -> The sum of all left leaves
    """
    # TODO: Implement this function
    if root is None:
        return sum
    
    if is_leaf_node(root.left):
        # print(root.left.val) 
        sum = sum + root.left.val
    else:
        sum = sum_of_left_leaves_helper(root.left, sum)

    if not is_leaf_node(root.right):    
        sum = sum_of_left_leaves_helper(root.right, sum)

    return sum

def sum_of_left_leaves(root):

    return  sum_of_left_leaves_helper(root, 0) 


root1, root2, root3, root4 = predefined_binary_trees()

print(sum_of_left_leaves(root4))