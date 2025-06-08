from common import Node, print_LL, take_input

def delete_at_tail(head):

    if head is None or head.next is None:
        return None
    
    temp = head
    while temp.next.next is not None:
        temp = temp.next

    temp.next = None
    return head

def delete_at_tail_recursive(head):

    if head is None:
        return None
    
    if head.next is None:
        return None
    
    head.next = delete_at_tail_recursive(head.next)

    return head

head_LL = take_input()
print_LL(head_LL)

# head_LL = delete_at_tail(head_LL)
# print("\nAfter deletion")
# print_LL(head_LL)

head_LL = delete_at_tail_recursive(head_LL)
print("\nAfter deletion recursively")
print_LL(head_LL)