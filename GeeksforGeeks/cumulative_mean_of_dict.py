"""
Given the dictionary list, our task is to write a Python Program to extract the mean of all keys.

    Input : test_list = [{‘gfg’ : 34, ‘is’ : 8, ‘best’ : 10},

                 {‘gfg’ : 1, ‘for’ : 10, ‘geeks’ : 9, ‘and’ : 5, ‘best’ : 12},

                 {‘geeks’ : 8, ‘find’ : 3, ‘gfg’ : 3, ‘best’ : 8}]

    Output : {‘gfg’: 12.666666666666666, ‘is’: 8, ‘best’: 10, ‘for’: 10, ‘geeks’: 8.5, ‘and’: 5, ‘find’: 3}
"""
            
from statistics import mean

test_list = [{'gfg' : 34, 'is' : 8, 'best' : 10},

             {'gfg' : 1, 'for' : 10, 'geeks' : 9, 'and' : 5, 'best' : 12},

             {'geeks' : 8, 'find' : 3, 'gfg' : 3, 'best' : 8}]

d= {}

for i in test_list:
    for j,k in i.items():
        if j in d:
           
            # combining each key to all values in
            # all dictionaries
            d[j].append(k)

        else:
            d[j] = [k]


for m, n in d.items():
    d[m] = mean(n)
print(d)
