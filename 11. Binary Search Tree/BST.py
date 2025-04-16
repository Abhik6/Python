from common import get_maximum, get_minimum

class BSTNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:

    def __init__(self):
        self.root = None

    def search_helper(self, data, root):
        if root is None:
            return False
        
        if root.val == data:
            return True
        
        if data < root.val:
            result = self.search_helper(data, root.left)
        else:
            result = self.search_helper(data, root.right)

        return result

    def search(self, data):

        return self.search_helper(data, self.root)
    

    def insert_helper(self, data, root):

        if root is None:
            new_node = BSTNode(data)
            root = new_node
            return root

        if data < root.val:
            root.left = self.insert_helper(data, root.left)
        else:
            root.right = self.insert_helper(data, root.right)

        return root


    def insert(self, data):

        self.root = self.insert_helper(data, self.root)


    def delete_helper(self, data, root):

        if root is None:
            return
        
        if root.val == data:

            if root.left is None: 
                return root.right
        
            if root.right is None:
                return root.left
            
            left_max = get_maximum(root.left)
            root.val = left_max
            root.left = self.delete_helper(left_max, root.left)

        elif data < root.val:
            root.left = self.delete_helper(data, root.left)
        else:
            root.right = self.delete_helper(data, root.right)        

        return root
        
    def delete(self, data):
        self.root = self.delete_helper(data, self.root) 
