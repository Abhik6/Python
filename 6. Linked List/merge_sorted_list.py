from common import *

def merge_sorted_list(head1,head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    new_head = None
    new_tail = None

    while head1 is not None and head2 is not None:
       
        if head1.data < head2.data:
            if new_head is None:
                new_head = head1
                new_tail = head1
            else:
                new_tail.next = head1
                new_tail = head1
            head1 = head1.next
            new_tail.next = None   
        else:
            if new_head is None:
                new_head = head2
                new_tail = head2
                
            else:
                new_tail.next = head2
                new_tail = head2
            head2 = head2.next
            new_tail.next = None 
        
        print("\nAfter iteration:")
        print_LL(new_head)
        print()
       
    if head1 is not None:
        new_tail.next = head1
    
    if head2 is not None:
        new_tail.next = head2
    
    print()

    return new_head

lst1 = [20,30,40,50,60,70]
head_LL1 = take_input_from_list(lst1)
print_LL(head_LL1)
print()

lst2 = [2,3,4,80,90,100]
head_LL2 = take_input_from_list(lst2)
print_LL(head_LL2)
print()

new_head = merge_sorted_list(head_LL1,head_LL2)
print_LL(new_head)
print()