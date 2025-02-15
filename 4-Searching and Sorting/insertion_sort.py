# def insertion_sort(lst):
#     # Your code goes here
#     n = len(lst)
#     for i in range(1,n):
#         for j in range(0,i):
#             if lst[i] < lst[j]:
#                 temp = lst[i]
#                 for k in range(i,j,-1):
#                     lst[k] = lst[k-1]
#                 lst[j] = temp
#         print(lst)
#     return lst

def insertion_sort(lst):

    n = len(lst)

    for current in range(1,n):
        currentCard = lst[current]
        correctPosition = current - 1
        # print(lst[current])
        while correctPosition >= 0:
            # print(correctPosition)
            # print(lst[current])
            if lst[correctPosition] < currentCard:
                # print(lst[correctPosition])
                # print(lst[current])
                # print("break position : ",correctPosition)
                break
            else:
                lst[correctPosition+1] = lst[correctPosition] # shifting operation
                correctPosition-=1
        # print(correctPosition+1)
        lst[correctPosition+1] = currentCard # insertion operation
        print(lst)
    return lst


unsorted_lst = [64, 25, 12, 22, 11]
print(f"Unsorted List : {unsorted_lst}")
sorted_lst = insertion_sort(unsorted_lst)
print(f"Sorted List : {sorted_lst}")