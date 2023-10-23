


def seperator_line(length):
    """
    

    Parameters
    ----------
    length : int
        Length of the seperator.

    Returns
    -------
    str
        Seperator line with length x.

    """
    return ("=" * length)

def batting_title():
    """
    

    Returns
    -------
    str
        Title String.

    """
    return ("\t\t\t\tBaseball Team Manager")

def batting_menu():
    """
    

    Returns
    -------
    str
        Menu Options.

    """
    return ("\nMENU OPTIONS\n1 - Calculate Batting Average\n2 - Exit Program")

def batting_average_calc(num_swings, num_hits):
    """
    

    Parameters
    ----------
    num_swings : int
        Number of attempts to hit.
    num_hits : int
        Number of successful hits.

    Returns
    -------
    batting_average : float
        Average number of balls hit.

    """
    batting_average = num_hits / num_swings
    
    return batting_average

def main():
    
    loop = 'y'
    
    print (seperator_line(60))
    
    print (batting_title())
    
    print (batting_menu())
    
    print (seperator_line(60))
    
    
    while loop == 'y':
        
        option = input("\nMenu Options: ")
    
        if option == '1':
            at_bats = int(input("\nOfficial Number of at Bats: "))
            hits = int(input("Number of Hits: "))
            average = (batting_average_calc(at_bats, hits))
            
            print ("Batting Average is {:.3f}".format(average))
            
        elif option == '2':
            print ("\nBye!")
            loop = False
            
        elif option == 'help':
           print (batting_menu())
            
        else:
            print ("\nNot a Valid Option. PLease Try Again")
    
if __name__ == "__main__":
    main()
    """
    For test, checking the following conditions
    1, 4, 0.25
    2, 4, 0.50
    3, 4, 0.75
    4, 4, 1
    """