# ----------------------------------------
# Program by K.R.S
#
#
# Version       Date        Info
# 1.0.0      2021-10-18     BinarySearch
#
# ----------------------------------------


def binarysearch(my_list, required_num, start, stop,):

    if start > stop:
        return False
    else:
        middle = (start + stop) // 2
        if required_num == my_list[middle]:
            return middle
        elif required_num < my_list[middle]:
            return binarysearch(my_list, required_num, start, stop - 1)
        else:
            return binarysearch(my_list, required_num, start + 1, stop)


my_list = [10, 12, 13, 15, 18, 20, 21, 23, 25, 27, 28, 32, 45, 49, 51, 65, 89]
required_num = 18
start = 0
stop = len(my_list)

x = binarysearch(my_list, required_num, start, stop)

if x == False:
    print("Item", required_num, "not found!")
else:
    print("Item", required_num, "found at index", x)
