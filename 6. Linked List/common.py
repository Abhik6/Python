class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def print_LL(head):
    temp = head
    while temp!=None:
        print(temp.data, end= "->")
        temp = temp.next

    return

def take_input():
    value = int(input("Enter an element: "))
    head = None
    tail = None

    while value != -1:
        newNode = Node(value)
        if head == None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        
        value = int(input("Enter an element: "))

    return head

def take_input_from_list(lst):
    head = None
    tail = None

    for value in lst:
        newNode = Node(value)
        if head == None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        
    return head


def length_LL(head):
    temp = head
    len = 0

    while temp!=None:
        len = len + 1
        temp = temp.next
    
    return len

def length_LL_recursive(head):

    if head == None:
        return 0

    recursive_ans = length_LL_recursive(head.next)

    ans = recursive_ans + 1

    return ans


# headLL = take_input()

# print_LL(headLL)
# print()
# print(length_LL(headLL))
# print(length_LL_recursive(headLL))
