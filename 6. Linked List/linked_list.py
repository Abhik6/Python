class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    
    def __init__(self):
        self.head = None

    def add_list_of_elements(self, lst):

        self.tail = None

        for elem in lst:
            new_node = Node(elem)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            
        return self

    def insert_elem_at_head(self, value):

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        return self

    def insert_elem_at_tail(self, value):

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return self
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = new_node

        return self

    def insert_elem_at_index(self, value, index):

        if index == 0:
            return self.insert_elem_at_head(value)

        if self.head is None:
            print("Index out of bounds")
            return self
        
        new_node = Node(value)

        temp = self.head
        count = 1

        while temp is not None and count < index:
            temp = temp.next
            count+=1
        
        new_node.next = temp.next
        temp.next = new_node

        return self
        

    

