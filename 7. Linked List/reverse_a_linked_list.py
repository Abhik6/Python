from common import *

def reverse_a_linked_list_optimized_recursive(head):

    if head is None or head.next is None:
        return head
    
    reversed_head = reverse_a_linked_list_optimized_recursive(head.next)

    reversed_tail = head.next
    reversed_tail.next = head
    head.next = None

    return reversed_head

def reverse_a_linked_list_recursive(head):
    pass

def reverse_a_linked_list_iteration(head):
    
    if head is None or head.next is None:
        return head
    
    previous = None
    current = head

    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous
        

lst1 = [20,30,40,50,60,70]
# lst1 = [20]
head_LL1 = take_input_from_list(lst1)
print_LL(head_LL1)
print()

head_LL = reverse_a_linked_list_iteration(head_LL1)
print_LL(head_LL)
