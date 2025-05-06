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
    
    def traverse(self):
        if self.head is None:
            return "None: None\n"
            
        
        temp = self.head
        str = ""
        while temp is not None:
            str = str + f"{temp.key}: {temp.value}\n"
            temp = temp.next
        return str


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
        self.size+=1

        return f"Inserted {key}: {value} in hashmap"

    def search(self, key):
        bucket_index = self.hash_function(key)
        bucket = self.slots[bucket_index]

        value = bucket.find(key)
        if value is None:
            return f"Key '{key}' not found"
        
        return value

    def delete(self, key):
        bucket_index = self.hash_function(key)
        bucket = self.slots[bucket_index]

        status = bucket.remove(key)
        self.size-=1

        if status:
            return f"Key '{key}' is removed"

        return f"Key '{key}' not found"
    
    def show(self):
        str = "{\n"
        for index in range(self.capacity):
            bucket = self.slots[index]
            str = str + bucket.traverse()
        str+="}"
        return str

    def __setitem__(self, key, value):
        status = self.insert(key, value)
        print(status)
    
    def __getitem__(self, key):
        value = self.search(key)
        print(value)
    
    def __str__(self):
        return self.show()

