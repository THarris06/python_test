# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:17:04 2023

@author: tyson.harris
"""

# deep copy method example
list1 = [1, 2, 3, 4, 5]
list2 = list1
list2[1] = 4

import copy
cp_list1 = [1, 2, 3, 4, 5]
cp_list2 = copy.deepcopy(cp_list1)
cp_list2[1] = 4

list_1 = [1, 2, 3, 4, 5]
list_2 = list_1.copy()
list_2[1] = 4

# slice function
slice_example = [20, 21, 22, 23, 24, 25, 26, 27]
slice_example[0:2]
slice_example[2:6]
# no defined stop/start does the entirity
slice_example[:3]
slice_example[4:]
# third number is step
slice_example[0:6:2]
# negative step allows us to count backwards
slice_example[::-1]
slice_example[6:2:-1]

# add lists together
concat_example = slice_example + list1

# Map method
def square(n):
    return n * n
squares_list_1 = map(square, list_1)
list(squares_list_1)

# filter method
def even_num(n):
    return n%2 == 0
evens = filter(even_num, slice_example)
b = list(evens)
print(b)

a = [x * x for x in list1]
print(a)