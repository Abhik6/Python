from common import *

root1, root2, root3 = predefined_binary_trees()

# print("BinaryTree1")
# print_binary_tree_recursive(root1)
# print("BinaryTree2")
# print_binary_tree_recursive(root2)
# print("BinaryTree3")
# print_binary_tree_recursive(root3)


# print("BinaryTree1")
# print_binary_tree_levelwise(root1)
# print("BinaryTree2")
# print_binary_tree_levelwise(root2)
# print("BinaryTree3")
# print_binary_tree_levelwise(root3)

# root = take_input_recursive()
# print_binary_tree_recursive(root)
# print()
# print_binary_tree_levelwise(root)

root = take_input_levelwise()
print_binary_tree_recursive(root)
print()
print_binary_tree_levelwise(root)
