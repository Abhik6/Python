from common import *

def postorder_traversal_helper(root, nodes=[]):

    if root is None:
        return []
    
    postorder_traversal_helper(root.left, nodes)
    postorder_traversal_helper(root.right, nodes)
    nodes.append(root.val)

    return nodes

def postorder_traversal(root):

    return postorder_traversal_helper(root, [])


root1, root2, root3, root4 = predefined_binary_trees()

print(postorder_traversal(root1))

print(postorder_traversal(root2))