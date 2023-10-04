
"""
 ,__,
(O,O)
/)_)
 ""
 
"""

print ("\nThe Test Scores Program\n")

print ("Enter 3 Test Scores\n======================")

score1 = int(input("Enter Test Score:\t"))
score2 = int(input("Enter Test Score:\t"))
score3 = int(input("Enter Test Score:\t"))

total = (score1 + score2 + score3)
average = (total / 3)

print ("======================")

print ("Total Score:\t{}".format(total))
print ("Average Score:\t{:.0f}".format(average))

if (average >= 90):
    grade = ("A")
    
elif (average <= 89 and average >= 80):
    grade = ("B")
    
elif (average <= 79 and average >= 60):
    grade = ("C")
    
elif (average <= 59 and average >= 40):
    grade = ("D")
        
elif (average <= 39 and average >= 0):
    grade = ("F")
    
else:
    grade = ("ERROR")

    
print ("Grade:\t{}".format(grade))

    
print ("\nBye!")

