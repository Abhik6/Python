
def max_depth(root):
    """
    Function to compute the maximum depth of a binary tree.
    :param root: TreeNode -> root of the binary tree
    :return: int -> maximum depth of the tree
    """
    if root is None:
        return 0

    Left_child_height = max_depth(root.left)
    right_child_height = max_depth(root.right)

    depth = 1 + max(Left_child_height, right_child_height)

    return depth
    