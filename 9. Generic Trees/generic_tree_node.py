class GenericTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    
def print_tree(root):
    if root is None:
        return

    print(root.data, end=":")

    for eachChild in root.children:
        print(eachChild.data, end=",")
    print()
    
    for eachChild in root.children:
        print_tree(eachChild)

root = GenericTreeNode(1)
child1 = GenericTreeNode(2)
child2 = GenericTreeNode(3)
child3 = GenericTreeNode(4)

root.children.append(child1)
root.children.append(child2)
child1.children.append(child3)

print_tree(root)

