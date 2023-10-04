# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:14:17 2023

@author: tyson.harris
"""

print ("\nBLACKJACK!")
print ("Blackjack payout is 3:2")
print ("Enter 'x' for outcome to Exit")

money = int(input("\nStarting Money:\t"))

loop = True

while loop:
    
    
    bet = input("\nBet Amount:\t")
    
    if (bet == 'x'):
        print ("\nBye!")
        break
    
    out = input("\nBlackjack, win, lose, or push:\t")
    
    if (out == 'b'):
        print ("\nENDING MONEY FOR A . . . \n")
        
        money = money + float(bet) * 1.5
        print ("Blackjack:\t{:.2f}".format(money))
            
    elif (out == 'w'):
        print ("\nENDING MONEY FOR A . . . \n")
        
        money = money + float(bet)
        print ("Win:\t{:.2f}".format(money))
        
    elif (out == 'l'):
        print ("\nENDING MONEY FOR A . . . \n")
        
        money = money - float(bet)
        print ("Lose:\t{:.2f}".format(money))
        
    elif (out == 'p'):
        print ("\nENDING MONEY FOR A . . . \n")
        
        print ("Push:\t{:.2f}".format(money))
    
    else:
        print("Invalid Input")


