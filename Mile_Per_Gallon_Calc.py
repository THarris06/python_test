"""
 ,__,
(O,O)
/)_)
 ""

"""

loop = 1

while (loop == 1):
    print ("\nThe Mile Per Gallon Program \n")

    miles = float(input("Enter Miles Driven: \t \t "))
    gallons = float(input("Enter Gallons of Gas Used: \t "))

    if (gallons > 0):
        print ("\nMiles Per Gallon: \t \t \t {:.2f}".format(miles / gallons))
        loop = 0

    else:
        print ("Gallons used must be greater than zero. Try again.")

print ("\nBye!")

