
from collections import deque

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

def sample_generic_trees():
    root1 = GenericTreeNode(1)
    child1 = GenericTreeNode(2)
    child2 = GenericTreeNode(3)
    child3 = GenericTreeNode(4)

    root1.children.append(child1)
    root1.children.append(child2)
    child1.children.append(child3)

    root2 = GenericTreeNode(1)
    child1 = GenericTreeNode(2)
    child2 = GenericTreeNode(3)
    child3 = GenericTreeNode(4)
    child4 = GenericTreeNode(5)
    child5 = GenericTreeNode(6)

    root2.children.append(child1)
    root2.children.append(child2)
    root2.children.append(child3)
    child1.children.append(child4)
    child4.children.append(child5)

    root3 = GenericTreeNode(1)
    child1 = GenericTreeNode(2)
    child2 = GenericTreeNode(3)
    child3 = GenericTreeNode(4)
    

    root3.children.append(child1)
    root3.children.append(child2)
    root3.children.append(child3)
    
    return root1, root2, root3

def take_input_levelwise():

    data = input("Enter data for root node : ")

    root = GenericTreeNode(data)

    queue = deque([root])

    while queue:
        current_node = queue.popleft()

        num_children = int(input(f"Enter number of children for node {current_node.data} : "))

        for i in range(1,num_children+1):

            node_data = input(f"Enter data for child {i} of node {current_node.data} : ")
            child_node = GenericTreeNode(node_data)
            current_node.children.append(child_node)
            queue.append(child_node)

    return root


