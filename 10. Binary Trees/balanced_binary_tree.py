
def is_balanced_helper(root):
    """
    Function to check if a binary tree is height-balanced.
    :param root: TreeNode -> root of the binary tree
    :return: bool -> True if the tree is balanced, False otherwise
    """
    
    if root is None:
        return True, 0
    
    is_left_balanced, left_height = is_balanced_helper(root.left)
    is_right_balanced, right_height = is_balanced_helper(root.right)

    height = 1 + max(left_height, right_height)

    height_diff = abs(left_height - right_height)

    if (not is_left_balanced) or (not is_right_balanced) or (height_diff > 1):
        return False, height
    
    return True, height

def is_balanced(root):

    balanced_flag, height = is_balanced_helper(root)

    return balanced_flag
     