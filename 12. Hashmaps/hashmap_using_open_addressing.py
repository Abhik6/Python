class Hashmap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None]*self.capacity
        self.values = [None]*self.capacity
        self.size = 0

    def hash_function(self, key):
        return abs(hash(key))
    
    def rehash(self, hash_value):
        # Linear Probing done to avoid collision
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
            # Update if key already present
            if self.slots[bucket_index] == key:
                self.values[bucket_index] = value
                return f"Updated {key}: {value} in hashmap"
            else:
                # Continue probing until an empty slot is found or key is found
                hash_value = self.rehash(hash_value)
                while bucket is not None and bucket != key:
                    hash_value = self.rehash(hash_value)
                    new_bucket_index = hash_value % self.capacity
                    bucket = self.slots[new_bucket_index]
                
                if bucket == key:
                    # Key already exists
                    self.values[new_bucket_index] = value
                    return f"Updated {key}: {value} in hashmap"
                else:
                    self.slots[new_bucket_index] = key
                    self.values[new_bucket_index] = value
                    self.size+=1
                    return f"Inserted {key}: {value} in hashmap"

    def get(self, key):

        hash_value = self.hash_function(key)
        initial_index = hash_value % self.capacity
        bucket = self.slots[initial_index]
        current_index = initial_index
        
        while bucket is not None: 
            if bucket == key:
                return self.values[current_index]

            hash_value = self.rehash(hash_value)
            current_index = hash_value % self.capacity
            bucket = self.slots[current_index]
            if current_index == initial_index:
                return f"Key '{key}' not present, traversed full"
        
        return f"Key '{key}' not present"
            

    def delete(self, key):

        hash_value = self.hash_function(key)
        initial_index = hash_value % self.capacity
        bucket = self.slots[initial_index]
        current_index = initial_index

        while bucket is not None:
            if bucket == key: 
                self.slots[current_index] = None
                self.values[current_index] = None
                self.size-=1
                return f"Key '{key}' is removed from hashmap"
            hash_value = self.rehash(hash_value)
            current_index = hash_value % self.capacity
            bucket = self.slots[current_index]
            if current_index == initial_index:
                return f"Key '{key}' not present, traversed full"

        return f"Key '{key}' not present"
        
  
    def show(self):

        result = "{\n"
        for i in range(self.capacity):
            if i == self.capacity-1:
                result+=f"{self.slots[i]} : {self.values[i]}\n"
            else:    
                result+=f"{self.slots[i]} : {self.values[i]},\n"
        result+="}"
        return result

    
    def __setitem__(self, key, value):
        return self.insert(key, value)


    def __getitem__(self, key):
        return self.get(key)
    
    def __str__(self):
        return self.show()
