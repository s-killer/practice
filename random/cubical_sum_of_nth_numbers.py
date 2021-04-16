# Sum of the cubes of the first n natural numbers

'''
#method 1:

n = int(input())
sum = 0
for i in range(n+1):
    # temp = input()
    #print("i",i)
    temp = i * i * i
    #print("cube",temp)
    sum += temp
print(sum)

'''

"""
#method 2:
sum = 0
for i in range( int(input())+1):
    sum += i * i * i
print(sum)
"""


#method 3:

print(sum([i*i*i for i in range(int(input())+1)]))

