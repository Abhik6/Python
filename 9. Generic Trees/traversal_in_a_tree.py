def preorder_traversal(root):

    if root == None:
        return

    print(root.data)

    for child in root.children:
        preorder_traversal(child)

def postorder_traversal(root):

    if root == None:
        return

    for child in root.children:
        postorder_traversal(child)

    print(root.data)