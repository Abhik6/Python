class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackUsingList:

    def __init__(self):
        self.__stack = [] ## Very very important to make private so that no one can access list directly

    def size(self):
        return len(self.__stack)
    
    def is_empty(self):
        return self.size() == 0
    
    def top(self):
        if self.is_empty():
            return f"Stack empty, no top element"

        return self.__stack[-1]

    def push(self, value):
        self.__stack.append(value)
        return f" {value} pushed into stack"
    
    def pop(self):
        if self.is_empty():
            return f"Stack empty, no element to pop"
        return self.__stack.pop()

class StackUsingLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0

    def size(self):
        return self.len

    def is_empty(self):
        return self.len == 0
    
    def push(self, value):
        new_node = Node(value)
        self.len+=1
        
        new_node.next = self.head
        self.head = new_node

        return f"{value} pushed into stack"
    
    def pop(self):

        if self.is_empty():
            return f"Stack empty, no element to pop"

        self.len-=1
        value_to_be_returned = self.head.data
        self.head = self.head.next

        return value_to_be_returned
    
    def top(self):

        if self.is_empty():
            return f"Stack empty, no top element"

        return self.head.data


    


