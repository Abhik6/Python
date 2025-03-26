from common import Node, print_LL, length_LL_recursive, length_LL, take_input
from insert_at_head import insert_at_head 

def insert_at_index(head, data, index):

    if index == 0:
        return insert_at_head(head, data)
    
    newNode = Node(data)
    temp = head
    count = 1

    while temp is not None and count < index:
        temp = temp.next
        count+= 1
    
    if temp is None:
        print("Out of bounds, provide correct index.")
        return head

    newNode.next = temp.next
    temp.next = newNode

    return head

# def insert_at_index_recursive(head, data, index, count=1):

#     if index == 0:
#         return insert_at_head(head, data)
    
#     if head is not None and index == count:
#         newNode = Node(data)
#         newNode.next = head.next
#         head.next = newNode
#         return head

    
#     if head is not None and count < index:
#         head.next = insert_at_index_recursive(head.next, data, index, count+1)
    

#     if head is None:
#         print("Out of bounds error, please provide correct index.")

#     return head

def insert_at_index_recursive(head, data, index):

    if index == 0:
        return insert_at_head(head, data)
    
    if head == None:
        print("Index out of bounds")
        return head

    head.next = insert_at_index_recursive(head.next, data, index-1)

    return head



head_LL = take_input()
print_LL(head_LL)

# head_LL = insert_at_index(head_LL, 100, 10)
# print("\nAfter Insertion at Index")
# print_LL(head_LL)

head_LL = insert_at_index_recursive(head_LL, 50, 0)
print("\nAfter Insertion at Index")
print_LL(head_LL)