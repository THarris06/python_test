# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:33:04 2023

@author: tyson.harris
"""

print (*range(10))

print (*range(5, 11))

print (*range(10, -31, -2))


for i in range (0, 11):
    print (i, end=" ")
    

print ("\nthe loop has ended")


b = 0

for a in range (1, 16):
   b += a
   
print(b)

