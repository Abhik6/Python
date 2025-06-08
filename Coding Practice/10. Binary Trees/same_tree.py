def is_same_tree(p, q):
    """
    Function to check if two binary trees are the same.
    :param p: TreeNode -> root of the first tree
    :param q: TreeNode -> root of the second tree
    :return: bool -> True if both trees are the same, False otherwise
    """
    
    if p is None and q is None:
        return True
    
    if (p is None and q is not None) or (q is None and p is not None):
        return False

    if p.val != q.val:
        return False
    
    is_same = is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right) 

    return is_same

