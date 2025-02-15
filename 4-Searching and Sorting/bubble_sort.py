def bubble_sort(lst):
    # Your code goes here
    size = len(lst)
    runs = size - 1
    indices = runs
    
    for run in range(0,runs):
        for index in range(0,indices):
            if lst[index] > lst[index+1]:
                var = lst[index+1]
                lst[index+1] = lst[index]
                lst[index] = var
        indices = indices - 1
        
    return lst

lst = [64, 34, 25, 12, 22, 11, 90]           
print(bubble_sort(lst))