# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 09:11:38 2023

@author: tyson.harris
"""

# Count: counts the number of times the value appears in a list
num_list = [1, 4, 4, 4, 4, 45, 78, 45, 17, 23, 65]

num_list.count(4)

fruits = ['apples', 'Apples', 'apples', 'apples', 
          'oranges', 'grapes', 'Kiwi']

fruits.count('apples')

# Reverse the order of the list
num_list.reverse()
print(num_list)

fruits.reverse()
print(fruits)

# Sorts int list from smallest to largest
num_list.sort()
num_list

# Sorts str list alphabetically
fruits.sort()
fruits
# use a key to sort defferently
fruits.sort(key=str.lower)
fruits

# Sorts and returns copy of the list
sorted(fruits)
sorted(fruits, key=str.lower)

max(num_list)
min(num_list)
sum(num_list)
sum(num_list, start = 200)
