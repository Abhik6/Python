from common import *

def rightSideView_helper(root, output_list=[]):
    # Implement your solution here
    if root is None:
        return []
    
    if len(output_list) == 0:
        output_list.append(root.val)

    if root.right is not None:
            output_list.append(root.right.val)

    rightSideView_helper(root.right, output_list)

    rightSideView_helper(root.left, output_list)

    return output_list

def rightSideView(root):
    return rightSideView_helper(root, [])

root1, root2, root3, root4 = predefined_binary_trees()

print(rightSideView(root4))




    