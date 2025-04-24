from common import *
from BST import *
from successor_and_predessessor_in_BST import *
from recover_BST import *
from bst_queries import *

root1, root2, root3, root4 = create_predefined_BST()
root5, root6 = create_predefined_binary_trees()

# print("BST 1")
# print_BST_levelwise(root1)
# print()
# print("BST 2")
# print_BST_levelwise(root2)
# print()
# print("BST 3")
# print_BST_levelwise(root3)
# print()
# print("BST 4")
# print_BST_levelwise(root4)


# print("BST 1")
# print_BST_inorder(root1)
# print()
# print("BST 2")
# print_BST_inorder(root2)
# print()
# print("BST 3")
# print_BST_inorder(root3)
# print()
# print("BST 4")
# print_BST_inorder(root4)


# print(search_elem_in_BST(root1, 100))
# print(search_elem_in_BST(root1, 15))

# lst1 = [10, 20, 30, 40, 50, 60, 70, 80]
# r1 = create_BST_from_sorted_list(lst1)
# print_BST_levelwise(r1)

# print(check_BST(root1))
# print(check_BST(root2))
# print(check_BST(root3))
# print(check_BST(root4))
# print(check_BST(root5))
# print(check_BST(root6))


# print(check_BST_Optimized(root1))
# print(check_BST_Optimized(root2))
# print(check_BST_Optimized(root3))
# print(check_BST_Optimized(root4))
# print(check_BST_Optimized(root5))
# print(check_BST_Optimized(root6))

# print_elements_in_range(root1, 12, 40)
# print()
# print_elements_in_range(root2, 10, 65)
# print()
# print_elements_in_range(root3, 4, 6)
# print()
# print_elements_in_range(root4, 5, 25)
# print()


# print(check_BST_limits(root1))
# print(check_BST_limits(root2))
# print(check_BST_limits(root3))
# print(check_BST_limits(root4))
# print(check_BST_limits(root5))
# print(check_BST_limits(root6))

# r1 = BST()
# r1.insert(20)
# r1.insert(30)
# r1.insert(15)
# r1.insert(25)
# r1.insert(50)
# r1.insert(5)

# print("Original Tree")
# print_BST_levelwise(r1.root)
# print_BST_inorder(r1.root)
# print()

# print(r1.search(20))
# print(r1.search(5))
# print(r1.search(30))
# print(r1.search(18))

# print("After deletion")
# r1.delete(20)
# print_BST_levelwise(r1.root)

# print(find_predecessor_successor(root1,15))
# print(find_predecessor_successor(root1,30))
# print(find_predecessor_successor(root1,5))
# print(find_predecessor_successor(root1,10))
# print(find_predecessor_successor(root1,20))

# print_BST_levelwise(recover_tree(root5))

queries = [[25,45], [0,50], [10,20], [50,100]]
print(count_nodes_in_range(root2, queries))