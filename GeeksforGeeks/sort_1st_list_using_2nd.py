# https://www.geeksforgeeks.org/python-sort-values-first-list-using-second-list/
"""
Sort the values of first list using second list
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
ans = ['a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g']

"""

list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

#list1 = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
#list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

l = len(list2)
list1 = list1[:l]

a = zip(list1,list2)
a = sorted(a, key=lambda x: x[1])
l4 = [i[0] for i in a]
print(l4)
