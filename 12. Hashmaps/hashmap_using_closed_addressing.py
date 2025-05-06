class LLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, key, value):
        temp = self.head
        
        while temp is not None:
            if temp.key == key:
                temp.value = value
                return 
            temp = temp.next
        
        if temp is None:
            new_node = LLNode(key, value)
            new_node.next = self.head
            self.head = new_node
        
        return 
    
    def find(self, key):

        temp = self.head

        while temp is not None:
            if temp.key == key:
                return temp.value 
            temp = temp.next

        return None

    def remove(self, key):
        prev = None
        curr = self.head

        while curr is not None:
            if curr.key == key and prev is None:
                self.head = curr.next
                return True
            elif curr.key == key and prev is not None:
                prev.next = curr.next
                return True
            else:
                prev = curr
                curr = curr.next       
        
        return False


class HashmapUsingClosedHashing:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.slots = [LinkedList() for i in range(self.capacity)]

    def hash_function(self, key):
        return abs(hash(key)) % self.capacity

    def insert(self, key, value):
        bucket_index = self.hash_function(key)
        bucket = self.slots[bucket_index]

        bucket.add(key, value)

        return f"Inserted {key}: {value} in hashmap"

    def search(self, key):
        bucket_index = self.hash_function(key)
        bucket = self.slots[bucket_index]

        value = bucket.find(key)
        if value is None:
            return f"Key '{key} not found"
        
        return value

    def delete(self, key):
        bucket_index = self.hash_function(key)
        bucket = self.slots[bucket_index]

        status = bucket.remove(key)
        
        if status:
            return f"Key '{key} is removed"

        return f"Key '{key} not found"
