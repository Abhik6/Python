from common import Node, print_LL, take_input_from_list

def delete_by_value(head, value):

    if head is None:
        return head
    
    if head.data == value:
        head = head.next
        return head
    
    temp = head
    count = 1

    while temp.next is not None and temp.next.data != value:
        temp = temp.next
        count+=1

    if temp.next is None:
        print("Value not present in list")
        return head

    temp.next = temp.next.next

    return head

def delete_by_value_recursive(head, value):

    if head is None:
        print("Value not present in list")
        return head
    
    if head.data == value:
        head = head.next
        return head
    
    head.next = delete_by_value_recursive(head.next, value)

    return head


lst = [20,30,40,50,60]
head_LL = take_input_from_list(lst)
print_LL(head_LL)
print()

head_LL = delete_by_value_recursive(head_LL, 30)
print("After Deletion")
print_LL(head_LL)
    

    
