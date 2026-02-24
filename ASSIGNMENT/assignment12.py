# You are given the following numbers: 
# 50,40,60,70 write a python code that multiply
# all these numbers together and print out the result. 
# Check if the total is equal 12000 if yes , divide this result by 5 and 
# add 5000 and print the final outcome.
# Else just add 3000 to the initials total and print out outcomes

# Solution
a = 50
b = 40
c = 60
d = 70
e = a*b*c*d
print("This is the result of multiplication" ,e)
if e == 12000:
    print("yes it is equal to 12000")
    newtotal = (e/5)+5000
    print(newtotal)
else:
    newtotal = e+3000
    print(newtotal)