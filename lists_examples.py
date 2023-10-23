# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 08:55:42 2023

@author: tyson.harris
"""

# Starting lists
# Syntax
"""
    list_name = [items1, items2, .....]
"""

movies = ["The Dark Knight", 2005, 9.99]
type(movies)

str_objects_list = ['sword', 'bat', 'cat']
flt_objects_list = [48.0, 88.0, 100.0, 40.0]

empty_list = []

scores = [0] * 10

flt_objects_list[0]
movies[0]

type(flt_objects_list[0])
type(str_objects_list[0])

flt_objects_list[-1]
flt_objects_list[-2]
flt_objects_list[-3]
flt_objects_list[-4]

flt_objects_list[2] = 'Hello!'
flt_objects_list[3] = False

movies.append(400)
movies.insert(2, "USA")
movies.remove("USA")
flt_objects_list.pop()
flt_objects_list.pop(1)

i = str_objects_list.index("bat")
str_objects_list.pop(i)

len(movies)
year = 2005
year in movies
year in str_objects_list
if (2005 in movies):
    movies.append("Class question")
    
for item in movies:
    print (item)
    
scores = [70, 80, 90, 100, 60]
total = 0
i = 0
while i < len(scores):
    total = total + scores[i]
    i = i + 1
print (total)

for j, item in enumerate(scores):
    print ("{} - {}".format(j, item))
    
cars = ["VW", "Ford", "BMW", "Audi"]
prices = [30000, 15000, 40000, 35000]
for c, p in zip(cars, prices):
    print ("{} - {}".format(c, p))

for i, item in enumerate(zip(cars, prices)):
    print ("{} - {}".format(i, item))
    

    
    
    
    
    
    
    
    