class LLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, key, value):          
        new_node = LLNode(key, value)
        new_node.next = self.head
        self.head = new_node
          
    def search(self, key):

        current = self.head

        while current is not None:
            if current.key == key:
                return current 
            current = current.next

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

    def rehash(self):
        print("Rehashing...")
        old_buckets = self.slots
        self.capacity = self.capacity*2
        self.slots = self.__createbuckets(self.capacity)
        self.size = 0 # Reset Size before reinserting elements

        for eachLinkedListHead in old_buckets:
            current = eachLinkedListHead.head
            while current is not None:
                self.insert(current.key, current.value)
                current = current.next
        print("Rehashing complete...")

    def hash_function(self, key):
        return abs(hash(key)) % self.capacity

    def insert(self, key, value):
        bucket_index = self.hash_function(key)
        bucket = self.slots[bucket_index]

        node = bucket.search(key)

        if node is None:
            bucket.add(key, value)
            self.size+=1
        else:
            node.value = value

        print(f"Inserted {key}: {value} in hashmap")

        load_factor = self.size/self.capacity
        print(f"Load Factor: {load_factor}")

        if load_factor > 0.75:
            self.rehash()

    def get(self, key):
        bucket_index = self.hash_function(key)
        bucket = self.slots[bucket_index]

        node = bucket.search(key)
        if node is None:
            return f"Key '{key}' not found"
        
        return node.value

    def delete(self, key):
        bucket_index = self.hash_function(key)
        bucket = self.slots[bucket_index]

        status = bucket.remove(key)
        
        if status:
            self.size-=1
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

    def __len__(self):
        return self.size
    
    def __str__(self):
        return self.show()

