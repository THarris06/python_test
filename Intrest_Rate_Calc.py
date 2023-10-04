# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 10:02:22 2023

@author: tyson.harris
"""



def future_value(monthly_invest, yearly_int, time_yrs):
    """
    

    Parameters
    ----------
    monthly_invest : FLOAT
        AMOUNT INVESTED MONTHLY.
    yearly_int : INT
        YEARLY INTREST RATE.
    time_yrs : INT
        NUMBER OF YEARS.

    Returns
    -------
    f_value : FLOAT
        FINAL VALUE AFTER 'X' YEARS.

    """
    m_time = y_time * 12
    m_int_rt = yearly_int / 12
    f_value = 0
    for i in range(m_time):
        f_value = monthly_invest + f_value
        f_value += (m_int_rt * f_value) / 100
    return f_value

loop = 'y'

while loop == 'y':
    
    mon_invest = float(input("\nEnter Monthly Investment:\t"))
    y_int_rt = int(input("Enter Yearly Intrest Rate:\t"))
    y_time = int(input("Enter Number of Years:\t\t"))
    
    future_val = future_value(mon_invest, y_int_rt, y_time)
    print ("Future Value:\t\t\t{}".format(future_val))
    
    loop = input("\nContinue? (y/n):\t")
    
print ("\nBye!")
