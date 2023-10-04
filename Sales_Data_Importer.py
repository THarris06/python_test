total = 0
loop = 'y'
a = 0

print ("SALES DATA IMPORTER\n")

print ("Enter sales data")


while loop == 'y':

    a += 1
    amount = float(input("\nAmount:\t\t\t"))
    year = int(input("Year:\t\t\t"))
    month = int(input("Month (1-12):\t"))
    day = int(input("Day (1-31):\t\t"))
    
    if month in range(1,4):
        quarter = 'Quarter 1'
        
    elif month in range(4,7):
        quarter = 'Quarter 2'
        
    elif month in range(7,10):
        quarter = 'Quarter 3'
        
    elif month in range(10,13):
            quarter = 'Quarter 4'
    
    total += amount
    
    print ("\n{}.\t\t\t\t{}-{}-{}\t\t{}\t\t${:.1f}\n".format(a, year, month, day, quarter, amount))
        
    loop = input("Enter more sales? (y/n): ")
                   
        
    if loop == 'n':
        break
        
    elif loop != 'y':
        print ("ERROR")
        break 

print ("\nTotal Sales")
print ("-" * 11)
print ("${:.1f}".format(total))

print("\nBye!")

