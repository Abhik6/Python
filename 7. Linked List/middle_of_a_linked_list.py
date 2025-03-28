from common import *

def middle_of_linked_list(head):

    if head is None:
        return None
    if head.next is None:
        return head

    len = length_LL(head)
    mid = len//2

    temp = head
    count = 0
    while count < mid - 1:
        temp = temp.next
        count+=1

    return temp

def middle_of_linked_list_slow_fast(head):

    slow = head
    fast = head

    while fast is not None and fast.next is not None:

        if head is None:
            return None
        
        if head.next is None:
            return head
        
        fast = fast.next.next
        slow = slow.next

    return slow

# lst = [20,30,40,50,60]
# # lst = [20]
# head_LL = take_input_from_list(lst)
# print_LL(head_LL)
# print()

# mid = middle_of_linked_list(head_LL)
# print(mid.data)