from common import Node, print_LL, length_LL_recursive, length_LL, take_input


def insert_at_tail(head, value):
    temp = head
    newNode = Node(value)

    if head is None:
        return newNode

    while temp.next != None:
        temp = temp.next

    temp.next = newNode

    return head


def insert_at_tail_recursive(head, value):

    
    if head == None:
        newNode = Node(value)
        return newNode 

    if head.next == None:
        newNode = Node(value)
        head.next = newNode
        return head

    head.next = insert_at_tail_recursive(head.next, value)

    return head

    
head_LL = take_input()
print_LL(head_LL)

new_head = insert_at_tail(head_LL, 100)
print("\nAfter Insertion:")
print_LL(new_head)

new_head_1 = insert_at_tail_recursive(head_LL, 100)
print("\nAfter Recursive Insertion:")
print_LL(new_head_1)



