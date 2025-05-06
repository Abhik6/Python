
from hashmap_using_open_addressing import *
from hashmap_using_closed_addressing import *

# dict = Hashmap(8)
dict = HashmapUsingClosedHashing(8)

print(dict.insert(1, "Apple"))
print(dict.insert(2, "Orange"))
print(dict.insert("Three", "Banana"))
print(dict.insert("Four", "Cherry"))
print(dict.show())
print()
print(dict.search("Three"))
print(dict.search(1))
print(dict.search(5))
print(dict.delete("Four"))
# dict.traverse()
print(dict.delete("Eight"))
print(dict.show())
dict['five'] = 'Apricot'
print()
print(dict.show())
dict['Three']

print(dict)