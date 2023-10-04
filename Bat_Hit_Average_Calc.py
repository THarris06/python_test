
"""

 ,__,
(O,O)
/)_)
 ""
 
"""
loop = True

print ("=" * 60)

print ("\t\t\t\tBaseball Team Manager")

print ("\nThis Program Calculates the Batting Average for a Player \nBased on the Player's Official Number of at Bats and Hits")


print ("\nMENU OPTIONS\n1 - Calculate Batting Average\n2 - Exit Program")
print ("=" * 60)


while loop:
    
    option = input("\nMenu Options: ")

    if option == '1':
        
        print ("\nCalculating Batting Average. . . ")
        name = input("\nPlayer's Name: ")
        at_bats = int(input("Official Number of at Bats: "))
        hits = int(input("Number of Hits: "))

        average = hits / at_bats


        print ('\n',name,"'s Batting Average is {:.3}".format(average))

    elif option == '2':
        print ("\nBye!")
        loop = False
    
    elif option == 'help':
        print ("\nHELP MENU\n1 - Calculate Batting Average\n2 - Exit Program")
    
    else:
        print ("\nNot a Valid Option. PLease Try Again")
        
