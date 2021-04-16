#https://www.codechef.com/problems/COVID19

#The virus will spread from an infected person to a non-infected person whenever the distance between them is at most 2
dist = 2
def check_spread(data_list):
    new_list = []
    spread = 1
    for i in range(len(data_list) -1):
        if data_list[i+1] - data_list[i] <= dist:
            spread += 1
        else:

            new_list.append(spread)
            spread  = 1
        if i == (len(data_list) -2):
            new_list.append(spread)
    return new_list


for i in range(int(input())):
    n  = int(input())
    l_list = list(map(int,input().split()))
    a = check_spread(l_list)
    print("=====",min(a),max(a))

