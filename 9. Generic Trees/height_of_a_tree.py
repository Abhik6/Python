def height_of_a_tree(root):
    if root == None: # Edge Case
        return 0
    
    height = 1
    max_height = 0

    for child in root.children:
        max_height = max(max_height, height_of_a_tree(child))

    height = height + max_height

    return height