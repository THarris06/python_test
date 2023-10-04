loop = 1

total = 0

prompt = 'o'

import random

print ("WELCOME TO BLACKJACK")


    
card1 = random.randint (1, 11)
card2 = random.randint (1, 11)
    
print (card1)
print (card2)
    
total = (card1 + card2)
    
print ("you have ",total,)
    
while prompt != 's':
        
    prompt = input ("hit or stand? (h/s) ")
        
    if prompt == 'h':
        total += random.randint (1, 11)
            
        print (total)
            
    if prompt == 's':
            
        opp_1 = random.randint (1, 11)
        opp_2 = random.randint (1, 11)
        opp_3 = random.randint (1, 11)
            
        opp_total = (opp_1 + opp_2 + opp_3)
            
        print ("opponent has ",opp_total,)
            
        
if total > 21:
    print ("You Lose")        
        
elif opp_total > 21:
    print ("You Lose")
    
elif total > opp_total:
        print ("You Win")
        
elif total < opp_total:
    print ("You Lose")
        
else:
    print ("draw")
    
    
        