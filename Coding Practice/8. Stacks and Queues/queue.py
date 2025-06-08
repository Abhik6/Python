class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueUsingList:

    def __init__(self):
        self.__queue = []

    def size(self):
        return len(self.__queue)
    
    def is_empty(self):
        return self.size() == 0
    
    def enqueue(self, value):
        self.__queue.append(value)

        return f"{value} added into queue"
    
    def dequeue(self):
        if self.is_empty():
            return f"Queue empty, no element to dequeue"
        return self.__queue.pop(0)
    
    def front(self):
        if self.is_empty():
            return f"Queue empty, no front element"
        return self.__queue[0]


class QueueUsingLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def size(self):
        return self.len
    
    def is_empty(self):
        return self.size() == 0
    
    def enqueue(self, value):
        new_node = Node(value)
        self.len+=1

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        return f"{value} added to queue"
    
    def dequeue(self):

        if self.is_empty():
            return f"Queue empty, no element to dequeue"
        
        self.len-=1
        value_to_be_returned = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return value_to_be_returned
    
    def front(self):

        if self.is_empty():
            return f"Queue empty, no front element"
        
        return self.head.data
        
        
