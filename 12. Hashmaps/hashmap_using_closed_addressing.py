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
            return "\nNone: None"
            
        
        temp = self.head
        str = "\n"
        while temp is not None:
            str = str + f"{temp.key}: {temp.value},"
            temp = temp.next
        return str[:-1]


class HashmapUsingClosedHashing:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.slots = self.__createbuckets(self.capacity)

    def __createbuckets(self, capacity):
        return [LinkedList() for i in range(capacity)]

    def rehash(self, capacity):
        print("Rehashing...")
        self.capacity = capacity
        self.size = 0
        new_slots = self.__createbuckets(self.capacity)

        for index in range(len(self.slots)):
            bucket = self.slots[index]
            temp = bucket.head
            while temp is not None:
                key = temp.key
                value = temp.value
                bucket_index = self.hash_function(key)
                new_bucket = new_slots[bucket_index]
                new_bucket.add(key, value)
                temp = temp.next
        self.slots = new_slots
        print("Rehashing complete...")

    def hash_function(self, key):
        return abs(hash(key)) % self.capacity

    def insert(self, key, value):
        bucket_index = self.hash_function(key)
        bucket = self.slots[bucket_index]

        bucket.add(key, value)
        self.size+=1
        print(f"Inserted {key}: {value} in hashmap")
        load_factor = self.size/self.capacity
        print(load_factor)

        if load_factor > 0.75:
            self.rehash(self.capacity*2)

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
        str = "{"
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

