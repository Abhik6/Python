from common import *

def preorder_traversal_helper(root, nodes=[]):

    if root is None:
        return []
    
    nodes.append(root.val)
    preorder_traversal_helper(root.left, nodes)
    preorder_traversal_helper(root.right, nodes)

    return nodes

def preorder_traversal(root):

    return preorder_traversal_helper(root, [])


root1, root2, root3, root4 = predefined_binary_trees()

print(preorder_traversal(root1))

print(preorder_traversal(root2))