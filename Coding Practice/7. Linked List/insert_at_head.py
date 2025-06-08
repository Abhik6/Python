from common import Node, print_LL, length_LL_recursive, length_LL, take_input

def insert_at_head(head, value):
    newNode = Node(value)
    newNode.next = head
    head = newNode

    return head

# head_LL = take_input()
# print_LL(head_LL)

# new_head = insert_at_head(head_LL, 100)
# print("\nAfter Insertion:")
# print_LL(new_head)

