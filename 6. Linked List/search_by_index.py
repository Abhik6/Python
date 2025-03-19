from common import Node, print_LL, take_input_from_list

def search_by_index(head, index):

    if head is None:
        return head
    
    temp = head
    count = 0

    while temp is not None and count < index:
        temp = temp.next
        count+=1

    if temp is None:
        print("Index out of bounds")
        return None
    
    value = temp.data

    return value

def search_by_index_recursive(head, index):

    if head is None:
        print("Index out of bounds")
        return None
    
    if index == 0:
        return head.data

    value = search_by_index_recursive(head.next, index-1)

    return value
    


lst = [20,30,40,50,60]
head_LL = take_input_from_list(lst)
print_LL(head_LL)
print()

index = search_by_index_recursive(head_LL, 5)
print("After Search")
print(index)