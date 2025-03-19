from common import Node, print_LL, take_input_from_list

def search_by_value(head, value):

    if head is None:
        return -1
    
    index = 0
    temp = head

    while temp is not None and temp.data != value:
        temp = temp.next
        index+=1
    
    if temp is None:
        return -1
    
    return index

def search_by_value_recursive(head, value, index = 0):

    if head is None:
        return -1
    
    if head.data == value:
        return index
    
    index = search_by_value_recursive(head.next, value, index+1)

    return index



lst = [20,30,40,50,60]
head_LL = take_input_from_list(lst)
print_LL(head_LL)
print()

index = search_by_value_recursive(head_LL, 40)
print("After Search")
print(index)
    