"""
https://www.geeksforgeeks.org/stock-buy-sell/

The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days.
 For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned by buying on day 0, selling on day 3.
 Again buy on day 4 and sell on day 6. If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.

"""
'''
stock_set = {100, 180, 260, 310, 40, 535, 695}

data = {}

current_max = None
if stock_set:
    current_max = stock_set[0]
    print("current_max--",current_max)


for i in stock_set:
    
    if i >= current_max:
        current_max = i
    else:
        # sell

'''



price = [100, 180, 260, 310, 40, 535, 695]
price = [200,100, 180, 260, 310, 40,10, 535, 234, 10, 180, 260, 310, 40,10, 535]
price = [100, 90,90,80,20]
n = len(price) - 1
#print('len',n)
current =  None
buy = None
sell = None
is_buy = False
for i in range(n):
    current = price[i]
    #print('current',current,i)
    if i ==0:
        # if 1st number is less than 2nd then buy
        if price[i+1] > current:
            buy = current
            is_buy = True
    else:
        if price[i+1] > current and not is_buy:
            #print("in 2nd if ", current, is_buy)
            #  100, 180, 260,
            # buy if next is greater
            buy = current
            is_buy = True
        elif price[i+1] < current and is_buy:
            # 100 , 40 and is_buy = True
            # then sell
            sell = current
            print("buy :", price.index(buy), "sell :", price.index(sell))
            is_buy = False
        else:
            #print("is_buy",is_buy,current, i )
            pass
    #print(i,n,is_buy, current)
    if i == (n -1) and is_buy:
        #print("--1")
        if price[i+1] > current:
            sell = price[i+1]
            print("buy :", price.index(buy), "sell :", price.index(sell))
            is_buy = False
