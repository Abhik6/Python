from common import *

def inorder_traversal_helper(root, nodes=[]):

    if root is None:
        return []

    inorder_traversal_helper(root.left, nodes)
    nodes.append(root.val)
    inorder_traversal_helper(root.right, nodes)

    return nodes

def inorder_traversal(root):

    return inorder_traversal_helper(root, [])


root1, root2, root3, root4 = predefined_binary_trees()

print(inorder_traversal(root1))

print(inorder_traversal(root2))