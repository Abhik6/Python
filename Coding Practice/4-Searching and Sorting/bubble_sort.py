def bubble_sort(lst):
    # Your code goes here
    size = len(lst)
    runs = size - 1
    indices = runs
    
    for run in range(0,runs):
        indices = size - 1 - run
        print(indices)
        for index in range(0,indices):
            if lst[index] > lst[index+1]:
                var = lst[index+1]
                lst[index+1] = lst[index]
                lst[index] = var
        print(lst)
    return lst

unsorted_lst = [5,4,3,2,1]#[] #[64, 34, 25, 12, 22, 11, 90]  
sorted_list = bubble_sort(unsorted_lst)       
print(f"Sorted list : {sorted_list}")