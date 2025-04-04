
def count_nodes_in_a_tree(root):
    if root == None:   # Edge Case
        return 0
    
    count = 1

    for child in root.children:
        count = count + count_nodes_in_a_tree(child)

    return count