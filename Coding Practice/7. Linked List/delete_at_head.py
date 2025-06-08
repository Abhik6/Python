from common import Node, print_LL, length_LL_recursive, length_LL, take_input

def delete_at_head(head):

    if head is None:
        return None
    
    head = head.next
    return head

head_LL = take_input()
print_LL(head_LL)

head_LL = delete_at_head(head_LL)
print("\nAfter deletion")
print_LL(head_LL)