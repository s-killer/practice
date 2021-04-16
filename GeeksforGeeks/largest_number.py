# Program to find largest element in an array
# https://www.geeksforgeeks.org/c-program-find-largest-element-array/
arr = [20, 10, 20, 4, 100]
largest = 0
for i in arr:
    if i > largest:
        largest = i
print(largest)
