# -*- coding: utf-8 -*-
"""
 ,__,
(O,O)
/)_)
 ""
"""

#def print_welcome ():
#    print ("Welcome")
#    print ("\n")
#    print ("Done with function")
#    
#print_welcome()

# def print_welcome (message):
#     print (message)
#     print ("\n")
#     print ("Done with the function")

# some_var = 'i am sleepy'
# print_welcome(some_var)

def calc_mpg(miles_driven, gallons_fuel):
    """
    This function calculates and returns miles per gallon

    Parameters
    ----------
    miles_driven : float or int
        Number of miles driven.
    gallons_fuel : float or int
        Gallons of fuel used.

    Returns
    -------
    mpg : float
        miles per gallon.

    """
    mpg = miles_driven / gallons_fuel
    return mpg

miles = 500
fuel = 14
calculated_mpg = calc_mpg(miles, fuel)
print (calculated_mpg)

print(calc_mpg(100, 10))

