# Write a python input that collects four numbers first_number, 
# second_number, third_number fourth_number 
# Find the sum of all these numbers and display(print) them out
# Now check if the sum is less than 4000 , 
# print it is less than 4000
# Immediately divide your total by 4 and 
# print out the final result
# Else Print sum  is greater than 4000 
# immediately subtract 200 from your sum and 
# print out the final result
# solution
print("enter your firstnumber")
firstnumber = float(input())
print("enter your secondnumber")
secondnumber = float(input())
print("enter your thirdnumber")
thirdnumber = float(input())
print("enter your fourtthnumber")
fourthnumber = float(input())
print("These are my details: ",firstnumber,  secondnumber, thirdnumber, fourthnumber)
total = firstnumber + secondnumber + thirdnumber + fourthnumber
print(total)
if total < 4000:
    print("yes it is less than 4000")
    newtotal = total/4
    print(newtotal)
else:
    print("no it is greater than 4000")
    newtotal = total - 200
    print(newtotal)