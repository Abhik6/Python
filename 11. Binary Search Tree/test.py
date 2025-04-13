from common import *

root1, root2, root3, root4 = create_predefined_BST()

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

lst1 = [10, 20, 30, 40, 50, 60, 70, 80]
r1 = create_BST_from_sorted_list(lst1)
print_BST_levelwise(r1)