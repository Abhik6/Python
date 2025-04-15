from collections import deque

class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create_predefined_binary_trees():

    root1 = BSTNode(5)
    child1 = BSTNode(3)
    child2 = BSTNode(6)
    child3 = BSTNode(2)
    child4 = BSTNode(8)
    child5 = BSTNode(1)
    child6 = BSTNode(7)
    root1.left = child1
    root1.right = child2
    child1.left = child3
    child1.right = child4
    child3.left = child5
    child2.right = child6

        #       5
        #     /   \
        #    3     6
        #   /  \    \
        #  2    8    7
        # /
        # 1         

    root2 = BSTNode(20)
    child1 = BSTNode(10)
    child2 = BSTNode(30)
    child3 = BSTNode(5)
    child4 = BSTNode(12)
    child5 = BSTNode(2)
    child6 = BSTNode(15)
    child7 = BSTNode(6)
    root2.left = child1
    root2.right = child2
    child1.left = child3
    child1.right = child4
    child3.left = child5
    child4.right = child6
    child6.right = child7

    #           20
    #         /   \
    #        10    30
    #       /  \    
    #      5    12    
    #     /      \
    #    2        15
    #              \
    #               6 


    return root1, root2


def create_predefined_BST():
    root1 = BSTNode(20)
    child1 = BSTNode(10)
    child2 = BSTNode(30)
    child3 = BSTNode(5)
    child4 = BSTNode(15)
    root1.left = child1
    root1.right = child2
    child1.left = child3
    child1.right = child4

        #       20
        #     /    \
        #    10     30
        #   /  \
        #  5    15

    root2 = BSTNode(50)
    child1 = BSTNode(20)
    child2 = BSTNode(70)
    child3 = BSTNode(10)
    child4 = BSTNode(30)
    child5 = BSTNode(60)
    child6 = BSTNode(100)
    root2.left = child1
    root2.right = child2
    child1.left = child3
    child1.right = child4
    child2.left = child5
    child2.right = child6

        #       50
        #     /    \
        #    20     70
        #   /  \   /  \
        #  10  30 60  100
            

    root3 = BSTNode(5)
    child1 = BSTNode(3)
    child2 = BSTNode(6)
    child3 = BSTNode(2)
    child4 = BSTNode(4)
    child5 = BSTNode(1)
    child6 = BSTNode(7)
    root3.left = child1
    root3.right = child2
    child1.left = child3
    child1.right = child4
    child3.left = child5
    child2.right = child6

        #       5
        #     /   \
        #    3     6
        #   /  \    \
        #  2    4    7
        # /
        # 1         


    root4 = BSTNode(20)
    child1 = BSTNode(10)
    child2 = BSTNode(30)
    child3 = BSTNode(5)
    child4 = BSTNode(12)
    child5 = BSTNode(2)
    child6 = BSTNode(15)
    child7 = BSTNode(18)
    root4.left = child1
    root4.right = child2
    child1.left = child3
    child1.right = child4
    child3.left = child5
    child4.right = child6
    child6.right = child7

    #           20
    #         /   \
    #        10    30
    #       /  \    
    #      5    12    
    #     /      \
    #    2        15
    #              \
    #               18 


    return root1, root2, root3, root4


def print_BST_levelwise(root):

    if root is None:
        return
    
    queue = deque([root])

    while queue:
        current_node = queue.popleft()

        print(current_node.val, end=":")

        if current_node.left is not None:
            print(f"L->{current_node.left.val}", end=" ")
            queue.append(current_node.left)
        else:
            print(f"L->None", end=" ")
        
        if current_node.right is not None:
            print(f"R->{current_node.right.val}")
            queue.append(current_node.right)
        else:
            print(f"R->None")
                  

def print_BST_inorder(root):
    if root is None:
        return
    
    print_BST_inorder(root.left)
    print(root.val, end=" ")
    print_BST_inorder(root.right)


def search_elem_in_BST(root, data):
    if root is None:
        return False
    
    if root.val == data:
        return True
    
    if data < root.val:
        result = search_elem_in_BST(root.left, data)
    else:
        result = search_elem_in_BST(root.right, data)

    return result


def create_BST_from_sorted_list_helper(lst, start, end):

    
    if len(lst) == 0:
        return None
    
    if start>=end:
        return None
    
    mid = start + (end-start)//2

    node_val = lst[mid]
    node = BSTNode(node_val)
    node.left = create_BST_from_sorted_list_helper(lst, start, mid)
    node.right = create_BST_from_sorted_list_helper(lst, mid+1, end)

    return node

    
def create_BST_from_sorted_list(lst):

    return create_BST_from_sorted_list_helper(lst, 0, len(lst))


def get_maximum(node):

    if node is None:
        return float("-inf")
    
    while node.right is not None:
        node = node.right

    maximum = node.val

    return maximum

def get_minimum(node):

    if node is None:
        return float("inf")
    
    while node.left is not None:
        node = node.left

    minimum = node.val

    return minimum    

def check_BST(root):
    
    if root is None:
        return True

    left_max = get_maximum(root.left)
    right_min = get_minimum(root.right)
    
    is_left_BST = check_BST(root.left)
    
    is_right_BST = check_BST(root.right)
    

    is_BST = is_left_BST and is_right_BST and (root.val > left_max) and (root.val < right_min)

    return is_BST

def check_BST_Optimized(root):

    if root is None:
        return float("-inf"), float("inf"), True
    
    left_max, left_min, is_left_BST = check_BST_Optimized(root.left)
    
    right_max, right_min, is_right_BST = check_BST_Optimized(root.right)

    is_BST = is_left_BST and is_right_BST and (root.val > left_max) and (root.val < right_min)

    maximum = max(root.val, right_max)
    minimum = min(root.val, left_min)

    return maximum, minimum, is_BST

def print_elements_in_range(root, low, high):

    if root is None:
        return
    
    if root.val>low:
        print_elements_in_range(root.left, low, high)
    
    if root.val>=low and root.val<=high:
        print(root.val, end=" ") 

    if root.val<high:
        print_elements_in_range(root.right, low, high)


def check_BST_limits_helper(root, low, high):

    if root is None:
        return True
    
    if root.val<low or root.val>high:
        return False
     
    is_left_BST = check_BST_limits_helper(root.left, low, root.val-1)
    is_right_BST = check_BST_limits_helper(root.right, root.val+1, high)

    is_BST = is_left_BST and is_right_BST

    return is_BST


def check_BST_limits(root):
    return check_BST_limits_helper(root, float("-inf"), float("inf"))

    