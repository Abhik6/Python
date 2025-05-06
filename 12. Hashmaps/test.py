
from hashmap_using_open_addressing import *

dict = Hashmap(8)

print(dict.insert(1, "Apple"))
print(dict.insert(2, "Orange"))
print(dict.insert("Three", "Banana"))
print(dict.insert("Four", "Cherry"))
dict.traverse()
print()
print(dict.search("Three"))
print(dict.search(1))
print(dict.search(5))
print(dict.delete("Four"))
# dict.traverse()
print(dict.delete("Eight"))
dict.traverse()
dict['five'] = 'Apricot'
print()
dict.traverse()
print(dict['Three'])