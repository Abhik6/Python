from common import *

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

print_elements_in_range(root1, 12, 40)
print()
print_elements_in_range(root2, 10, 65)
print()
print_elements_in_range(root3, 4, 6)
print()
print_elements_in_range(root4, 5, 25)
print()