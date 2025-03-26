from common import *
from middle_of_a_linked_list import *
from merge_sorted_list import *

def merge_sort_linked_list(head):

    print_LL(head)
    print()

    if head is None or head.next is None:
        return head
    
    mid = middle_of_linked_list(head)

    head1 = head
    head2 = mid.next
    mid.next = None

    sorted_head1 = merge_sort_linked_list(head1)
    sorted_head2 = merge_sort_linked_list(head2)

    print("\nSorted head1:")
    print_LL(sorted_head1)
    print()
    print("Sorted head2:")
    print_LL(sorted_head2)
    print()
    sorted_merged_head = merge_sorted_list(sorted_head1, sorted_head2)
    print("Sorted Merged head:")
    print_LL(sorted_merged_head)

    return sorted_merged_head


lst = [5, 9, 2, 1, 18, 4, 6, 15, 13]
# lst1 = [20]
head_LL = take_input_from_list(lst)
print_LL(head_LL)
print()

sorted_head = merge_sort_linked_list(head_LL)
print("\nAfter sorting:")
print_LL(sorted_head)
print()