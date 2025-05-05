class Hashmap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None]*self.capacity
        self.values = [None]*self.capacity
        self.size = 0

    def hash_function(self, key):
        return abs(hash(key))
    
    def linear_probe(self, hash_value):
        return hash_value+1

    def insert(self, key, value):

        hash_value = self.hash_function(key)
        bucket_index = hash_value % self.capacity
        bucket = self.slots[bucket_index]

        if bucket is None:
            self.slots[bucket_index] = key
            self.values[bucket_index] = value
            self.size+=1
            return f"Inserted {key}: {value} in hashmap"
        else:
            while bucket is not None and bucket != key:
                hash_value = self.linear_probe(hash_value)
                new_bucket_index = hash_value % self.capacity
                bucket = self.slots[new_bucket_index]
            
            if bucket == key:
                self.values[new_bucket_index] = value
            else:
                self.slots[new_bucket_index] = key
                self.values[new_bucket_index] = value
                self.size+=1
                return f"Inserted {key}: {value} in hashmap"

    def search(self, key):

        hash_value = self.hash_function(key)
        bucket_index = hash_value % self.capacity
        bucket = self.slots[bucket_index]
        current = bucket
        
        while current is not None and current != key: 

            hash_value = self.linear_probe(hash_value)
            bucket_index = hash_value % self.capacity
            current = self.slots[bucket_index]
            if current == bucket:
                return f"Key '{key}' not present"

        if current is None:
            return f"Key '{key}' not present"
        else:
            return f"Value for Key '{key}' is {self.values[bucket_index]}"

    
    def delete(self, key):

        hash_value = self.hash_function(key)
        bucket_index = hash_value % self.capacity
        bucket = self.slots[bucket_index]
        current = bucket

        while current is not None and current != key: 
            hash_value = self.linear_probe(hash_value)
            bucket_index = hash_value % self.capacity
            current = self.slots[bucket_index]
            if current == bucket:
                return f"Key '{key}' not present"

        if current is None:
            return f"Key '{key}' not present"
        else: 
            self.slots[bucket_index] = None
            self.values[bucket_index] = None
            self.size-=1
            return f"Key '{key}' is removed from hashmap"
        
    
    def traverse(self):

        print("{")
        for i in range(self.capacity):
            if i == self.capacity-1:
                print(f"{self.slots[i]} : {self.values[i]}")
            else:    
                print(f"{self.slots[i]} : {self.values[i]},")
        print("}")


