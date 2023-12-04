#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    number = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            number[count] = True
        else:
            number[count] = False
    return (number)
