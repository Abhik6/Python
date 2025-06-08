from linked_list import *
from common import *

lst = [30, 40, 50, 60, 70]

ll = Linked_List()
# print(dir(ll))
ll = ll.add_list_of_elements(lst)
print_LL(ll.head)

# # print(head_LL)
ll = ll.insert_elem_at_head(10)
print_LL(ll.head)
# print(dir(ll))

ll = ll.insert_elem_at_tail(100)
print_LL(ll.head)

ll = ll.insert_elem_at_index(80, 7)
print_LL(ll.head)

# ll = ll.delete_elem_at_head()
# print_LL(ll.head)

# ll = ll.delete_elem_at_tail()
# print_LL(ll.head)

# ll = ll.delete_elem_at_index(10)
# print_LL(ll.head)

# ll = ll.delete_elem_by_value(100)
# print_LL(ll.head)

# value = ll.get_elem(8)
# print(value)

value = ll.is_elem_present(2)
print(value)