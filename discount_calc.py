
"""
 ,__,
(O,O)
/)_)
 ""
 
"""

print ("\nProgram for Customer Discounts")
print ("==================================")


customer_type = input("Enter Cutomer Type (R/W) :\t")

invoice_total = int(input("Enter Invoice Total:\t\t"))

if customer_type.lower() == "r":
    if invoice_total < 250:
        discount_per = (0)
        
            
    elif invoice_total >= 250:
        discount_per = (.2)
        
            
elif customer_type.lower() == "w":
    discount_per = .4

            
else:
    print("Customer type must be R or W.")
    
    
total = (invoice_total - invoice_total * discount_per)
print ("==================================")
print ("Invoice Total:   {:.0f}".format(invoice_total))
print ("Discount Percet: {}".format(discount_per))
print ("Total Discount:  {:.0f}".format(invoice_total * discount_per))
print ("Your total is:   {:.0f}".format(total))

print ("\nBye!")