# def selection_sort(lst):
#     # Your code goes here
#     size = len(lst)
#     runs = size - 1
    
#     for run in range(runs):
#         start_index = run
#         min_index = run
#         min = lst[min_index]
#         # print(min)
#         for index in range(run+1, size):
#             # print(index)
#             if lst[index]<min:
#                 # print("index:",index)
#                 min = lst[index]
#                 min_index = index
#                 # print("min index:", min_index)
#         # print(min_index)
#         lst[start_index], lst[min_index] = lst[min_index], lst[start_index]
#         print(lst)
#     return lst

def selection_sort(lst):
    # Your code goes here
    n = len(lst)
    
    for i in range(n-1):
        min_index = i
        # print(min)
        for j in range(i+1, n):
            # print(index)
            if lst[j]<lst[min_index]:
                # print("index:",index)
                min_index = j
                # print("min index:", min_index)
        # print(min_index)
        lst[i], lst[min_index] = lst[min_index], lst[i]
        print(lst)
    return lst  
    
unsorted_lst = [64, 25, 12, 22, 11]
print(f"Unsorted List : {unsorted_lst}")
sorted_lst = selection_sort(unsorted_lst)
print(f"Sorted List : {sorted_lst}")