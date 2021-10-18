# ----------------------------------------
# Program by K.R.S
#
#
# Version       Date        Info
# 1.0.0      2021-10-18     Bubble Sort
#
# ----------------------------------------

oldlist = [10, 75, 123, -4, 15, 32, 8, 27]

def bubble_sort(my_list):

    last_item = len(my_list) - 1

    for z in range(0, last_item):
        for x in range(0, last_item - z):
            if my_list[x] > my_list[x + 1]:
                my_list[x], my_list[x + 1] = my_list[x + 1], my_list[x]

    return my_list

print("Old list:", oldlist)
newlist = bubble_sort(oldlist).copy()
print("New list:", newlist)
