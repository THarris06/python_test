
# loop = True

# print ("=" * 60)

# print ("\t\t\t\tBaseball Team Manager")

# print ("\nThis Program Calculates the Batting Average for a Player \nBased on the Player's Official Number of at Bats and Hits")


# print ("\nMENU OPTIONS\n1 - Calculate Batting Average\n2 - Exit Program")
# print ("=" * 60)


# while loop:
    
#     option = input("\nMenu Options: ")

#     if option == '1':
        
#         print ("\nCalculating Batting Average. . . ")
#         name = input("\nPlayer's Name: ")
#         at_bats = int(input("Official Number of at Bats: "))
#         hits = int(input("Number of Hits: "))

#         average = hits / at_bats


#         print ('\n',name,"'s Batting Average is {:.3}".format(average))

#     elif option == '2':
#         print ("\nBye!")
#         loop = False
    
#     elif option == 'help':
#         print ("\nHELP MENU\n1 - Calculate Batting Average\n2 - Exit Program")
    
#     else:
#         print ("\nNot a Valid Option. PLease Try Again")
        
    
def seperator_line(length):
    return ("=" * length)
    
def batting_title():
    return ("\t\t\t\tBaseball Team Manager")

def batting_menu():
    return ("\nMENU OPTIONS\n1 - Calculate Batting Average\n2 - Exit Program")

def batting_average_calc(num_swings, num_hits):
    num_swings = int(input("Official Number of at Bats: "))
    num_hits = int(input("Number of Hits: "))
    
    batting_average = num_hits / num_swings
    
    return batting_average

if __name__ == "__main__":
    
    loop = 'y'
    
    print (seperator_line(60))
    
    print (batting_title())
    
    print (batting_menu())
    
    