from common import Node, print_LL, take_input_from_list

def delete_node_at_index(head, index):

    if head is None:
        print("Index out of bounds")
        return head
    
    if index == 0:
        head = head.next
        return head
    
    temp = head
    count = 1

    while temp is not None and count < index:
        temp = temp.next
        count+=1

    if temp is None or temp.next is None:
        print("Index out of bounds")
        return head

    temp.next = temp.next.next

    return head

def delete_node_at_index_recursive(head, index):

    if head is None:
        print("Index out of bounds")
        return head
    
    if index == 0:
        head = head.next
        return head

    head.next = delete_node_at_index_recursive(head.next, index-1)

    return head


lst = [20,30,40,50,60]
head_LL = take_input_from_list(lst)
print_LL(head_LL)
print()

head_LL = delete_node_at_index_recursive(head_LL, 4)
print("After Deletion")
print_LL(head_LL)








    
