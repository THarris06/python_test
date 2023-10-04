# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 08:59:47 2023

@author: tyson.harris
"""

def calc_mpg(miles_driven, gallons_fuel):
    """
    

    Parameters
    ----------
    miles_driven : float
        Enter Miles Driven.
    gallons_fuel : float
        Enter Gallons of Fuel Burned.

    Returns
    -------
    miles_per_gallon : Float
        Miles Driven per Gallon Burned.

    """
    miles_per_gallon = miles_driven / gallons_fuel
    return miles_per_gallon

if __name__ == "__main__":
    
    loop = 'y'
    
    print ("\nThe Mile Per Gallon Program")
    
    while loop.lower() == 'y':
        
        miles = float(input("\nEnter Miles Driven:\t\t"))
        gallons = float(input("Enter Gallons of Gas Used:\t"))
    
        if (gallons > 0):
            mpg = calc_mpg(miles, gallons)
            print("\nMiles Per Gallon:\t\t\t{:.2f}".format(mpg))
    
        else:
            print ("Gallons used must be greater than zero. Try again.")
            
        loop = input("\nContinue? (y/n): ")
        
        if loop != 'y' or 'n':
            print ("Invalid Input")
            break
        
    print ("\nBye!")
    
