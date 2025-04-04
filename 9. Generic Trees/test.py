from common import *
from count_nodes_in_a_tree import *
from height_of_a_tree import *
from traversal_in_a_tree import *

# root = take_input_levelwise()

# print_tree(root)

root1, root2, root3 = sample_generic_trees()

# print("Counts:")
# count1 = count_nodes_in_a_tree(root1)
# print(count1)

# count2 = count_nodes_in_a_tree(root2)
# print(count2)

# count3 = count_nodes_in_a_tree(root3)
# print(count3)

# print("Heights:")
# height1 = height_of_a_tree(root1)
# print(height1)

# height2 = height_of_a_tree(root2)
# print(height2)

# height3 = height_of_a_tree(root3)
# print(height3)

# print("Pre order Traversal")
# print("Root1")
# preorder_traversal(root1)
# print("Root2")
# preorder_traversal(root2)
# print("Root3")
# preorder_traversal(root3)

print("Post order Traversal")
print("Root1")
postorder_traversal(root1)
print("Root2")
postorder_traversal(root2)
print("Root3")
postorder_traversal(root3)