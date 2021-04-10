# Sorting using another list without built-in sort, min, max function -- bubble sort

# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements 
# if they are in wrong order


def sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                

arr = [20, 3, 15, 1, 6, 9, 2]
arr = [9, 14, -5, 1, 77, 16,-3, -3, 1]
arr = [-5, -23, 5, 0, 23, -6, 23, 67]
arr = [64, 34, 25, 12, 22, 11, 90]

print("initial",arr)
sort(arr)
print(arr)

