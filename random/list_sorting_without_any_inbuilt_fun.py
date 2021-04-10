# Sorting using another list without built-in sort, min, max function
# it creates new list

def sort(arr):

    new_list = []

    while arr:
        minimum = arr[0]  # arbitrary number in list 
        for x in arr: 
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        arr.remove(minimum)    

    print new_list

arr = [20, 3, 15, 1, 6, 9, 2]
arr = [9, 14, -5, 1, 77, 16,-3, -3, 1]
arr = [-5, -23, 5, 0, 23, -6, 23, 67]
print("initial",arr)
sort(arr)
