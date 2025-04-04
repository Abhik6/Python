from collections import deque

class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def predefined_binary_trees():

    root1 = BinaryTreeNode(1)
    child1 = BinaryTreeNode(2)
    child2 = BinaryTreeNode(3)
    child3 = BinaryTreeNode(4)
    child4 = BinaryTreeNode(5)
    root1.left = child1
    root1.right = child2
    child1.left = child3
    child1.right = child4

        #       1
        #     /   \
        #    2     3
        #   /  \
        #  4    5

    root2 = BinaryTreeNode(1)
    child1 = BinaryTreeNode(2)
    child2 = BinaryTreeNode(3)
    child3 = BinaryTreeNode(4)
    child4 = BinaryTreeNode(5)
    child5 = BinaryTreeNode(6)
    child6 = BinaryTreeNode(7)
    root2.left = child1
    root2.right = child2
    child1.left = child3
    child1.right = child4
    child2.left = child5
    child2.right = child6

        #       1
        #     /   \
        #    2     3
        #   /  \  /  \
        #  4    5 6   7
            

    root3 = BinaryTreeNode(1)
    child1 = BinaryTreeNode(2)
    child2 = BinaryTreeNode(3)
    child3 = BinaryTreeNode(4)
    child4 = BinaryTreeNode(5)
    child5 = BinaryTreeNode(6)
    child6 = BinaryTreeNode(7)
    root3.left = child1
    root3.right = child2
    child1.left = child3
    child1.right = child4
    child3.left = child5
    child2.right = child6

        #       1
        #     /   \
        #    2     3
        #   /  \    \
        #  4    5    7
        # /
        # 6         


    root4 = BinaryTreeNode(1)
    child1 = BinaryTreeNode(2)
    child2 = BinaryTreeNode(3)
    child3 = BinaryTreeNode(4)
    child4 = BinaryTreeNode(5)
    child5 = BinaryTreeNode(6)
    child6 = BinaryTreeNode(7)
    child7 = BinaryTreeNode(8)
    root4.left = child1
    root4.right = child2
    child1.left = child3
    child1.right = child4
    child3.left = child5
    child4.right = child6
    child6.right = child7

    #           1
    #         /   \
    #        2     3
    #       /  \    
    #      4    5    
    #     /      \
    #    6        7
    #              \
    #               8 


    return root1, root2, root3, root4


def print_binary_tree_recursive(root):

    if root is None:
        return
    
    print(root.val, end=":")

    if root.left is not None:
        print(f"L->{root.left.val}",end=" ")
    else:
        print(f"L->None",end=" ")

    if root.right is not None:
        print(f"R->{root.right.val}")
    else:
        print(f"R->None")

    print_binary_tree_recursive(root.left)
    print_binary_tree_recursive(root.right)


def print_binary_tree_levelwise(root):
    # This is also call Breadth First Search (BFS)
    # We use a queue to implement this

    queue = deque([root])

    while queue:
        current_node = queue.popleft()

        print(current_node.val, end=":")

        if current_node.left:
             print(f"L->{current_node.left.val}", end=" ")
             queue.append(current_node.left)
        else:
            print(f"L->None", end=" ")

        if current_node.right:
             print(f"R->{current_node.right.val}")
             queue.append(current_node.right)
        else:
            print(f"R->None")

def take_input_recursive():

    data = int(input("Enter data for the node: "))

    if (data == -1):
        return None
    
    node = BinaryTreeNode(data)

    print(f"Enter left child for node {data}: ")
    node.left = take_input_recursive()
    print(f"Enter right child for node {data}: ")
    node.right = take_input_recursive()

    return node

def take_input_levelwise():

    val = int(input("Enter the data for root: "))

    if val == -1:
        return None
    
    root = BinaryTreeNode(val)

    queue = deque([root])

    while queue:
        current_node = queue.popleft()

        left_data = int(input(f"Enter data for left child of {current_node.val}: "))

        if left_data != -1:
            current_node.left = BinaryTreeNode(left_data)
            queue.append(current_node.left)
        else:
            current_node.left = None
        
        right_data = int(input(f"Enter data for right child of {current_node.val}: "))

        if right_data != -1:
            current_node.right = BinaryTreeNode(right_data)
            queue.append(current_node.right)
        else:
            current_node.right = None

    return root

def height_of_binary_tree(root):
    
    if root is None:
        return 0

    Left_child_height = height_of_binary_tree(root.left)
    right_child_height = height_of_binary_tree(root.right)

    height = 1 + max(Left_child_height, right_child_height)

    return height

def diameter_of_binary_tree(root):

    if root is None:
        return 0
    
    left_height = height_of_binary_tree(root.left)
    right_height = height_of_binary_tree(root.right)

    left_diameter = diameter_of_binary_tree(root.left)
    right_diameter = diameter_of_binary_tree(root.right)

    ans_diamter = max(left_diameter, right_diameter, left_height + right_height)

    return ans_diamter

def diameter_of_binary_tree_optimized(root):

    if root is None:
        return 0,0
    
    left_height, left_diameter = diameter_of_binary_tree_optimized(root.left)
    right_height, right_diameter = diameter_of_binary_tree_optimized(root.right)
    
    diameter = max(left_diameter, right_diameter, left_height+right_height)

    height = 1 + max(left_height, right_height)

    return height, diameter

def is_binary_tree_balanced(root):

    if root is None:
        return True
    
    left_height = height_of_binary_tree(root.left)
    right_height = height_of_binary_tree(root.right)

    if abs(left_height - right_height) > 1:
        return False
    else:
        is_left_balanced = is_binary_tree_balanced(root.left)
        is_right_balanced = is_binary_tree_balanced(root.right)
        if (not is_left_balanced) or (not is_right_balanced):
            return False

    return True    

def is_binary_tree_balanced_optimized(root):

    if root is None:
        return True, 0
    
    is_left_balanced, left_height = is_binary_tree_balanced_optimized(root.left)
    is_right_balanced, right_height = is_binary_tree_balanced_optimized(root.right)

    height = 1 + max(left_height, right_height)

    height_diff = abs(left_height - right_height)

    if (not is_left_balanced) or (not is_right_balanced) or (height_diff > 1):
        return False, height
    
    return True, height




