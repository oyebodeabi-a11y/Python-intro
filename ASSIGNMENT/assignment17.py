# You are given the following 2.56.78.34.23,21 in a list.
# Write a python code that add all the numbers together as total. 
# Check if the total is greater than 50 ,
# if yes divide this result by 20 and add 19 and 
# print final outcome Else just add 500 to the initials total and 
# print out outcomes

# solution
a = 2
b = 56
c = 78
d = 34
e = 23
f = 21
total = a+b+c+d+e+f
print(total)
if total > 50:
    print("total is greater than 50")
    newtotal = (total/20)+19
    print(newtotal)
else:
    newtotal = total+500
    print(newtotal)