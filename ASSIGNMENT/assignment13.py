# You are given the following numbers: 500,120,478,200 
# write a python code thatadds all these numbers together 
# and print out the result. Check if the total is greater than 120 
# if yes , multiply this result by 5 and add 140 and print the finaloutcome.
# Else just subtract 450 from the initials total and print out outcomes.

# solution
a = 500
b = 120
c = 478
d = 200
e = a+b+c+d
print("this is the result: ", e)
if e > 120:
    print("yes it is the greater than 120")
    newtotal = (e*5)+140
    print(newtotal)
else:
    newtotal = e-450
    print(newtotal)
    
