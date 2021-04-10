# Sorting using another list without built-in sort, min, max function
# it creates new list

def sort(data_list):
    min = ''
    max = ''
    min = data_list[0]
    max = data_list[0]
    sl = []

    for i in data_list:
        if min >= i:
            # because minimun valus is greater than i
            # appending i at the starting of the list
            sl.insert(0,i)
            min = i
        else:
            if max == i :
                sl.append(i)
            elif max < i:
                # max = 40 , i = 80
                # i > max so appending in the sorted list
                # max = i
                sl.append(i)
                max = i
            else:
                # in this case i is between min and max
                for s in sl:
                    # looping through sorted list and
                    # checking for the number greater than i
                    if s >= i:
                        # inserting at the index of s
                        sl.insert(sl.index(s),i)
                        break
    print(sl)


data_list = [20, 3, 15, 1, 6, 9, 2]
data_list = [9, 14, -5, 1, 77, 16,-3, -3, 1]
data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
sort(data_list)

