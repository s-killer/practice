# https://www.hackerrank.com/challenges/calendar-module/problem

import calendar
if __name__ =="__main__":
    d,m, y = input().split()
    l = ["sunday","Monday","tuesday", "Wednesday", "Thursday", "Friday",  "Saturday"]
    print(int(y))
    if (int(y) > 2000 and int(y) < 3000):
        index = calendar.weekday(int(y),int(m),int(d))
        print(l[index-1].upper())
