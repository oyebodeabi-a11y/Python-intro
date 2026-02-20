# Write a python input that collects three numbers first_number, second_number, third_number 
# Find the total of all these numbers and display(print) them out
# Now check if the total is greater than 2000 , print it is greater than 2000
# Immediately multiply your total by 50 and print out the final result
# Else Print total  is less than 2000
# immediately multiply your total by 3 and print out the final result

# Solution
print("enter your firstnumber")
firstnumber = float(input())
print("enter your secondnumber")
secondnumber = float(input())
print("enter your thirdnumber")
thirdnumber = float(input())
print("These are the numbers: ",firstnumber,  secondnumber, thirdnumber)
total = firstnumber + secondnumber + thirdnumber
print(total)
if total > 2000:
    print("it is greater than 2000")
    newtotal = total*50
    print(newtotal)
else:
    print("total  is less than 2000")
    newtotal = total*3
    print(newtotal)