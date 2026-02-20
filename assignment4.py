# Write a python input that collects three numbers first_number, second_number, third_number 
# Find the total of all these numbers and display(print) them out
# Now check if the total is equal 3000 , print it is less than 3000
# Immediately divide your total by 4 and print out the final result
# Else Print sum  is greater than 3000
# immediately subtract 300 from your sum and print out the final result

# solution
print ("enter the firstnumber")
firstnumber = float(input())
print ("enter the secondnumber")
secondnumber = float(input())
print("enter the thirdnumber")
thirdnumber = float(input())
total = firstnumber+secondnumber+thirdnumber
print(total)
if total==3000:
    print("it is less than 3000")
    newtotal = total/4
    print(newtotal)
else:
    print("sum is greater than 3000")
    newtotal = total - 300
    print(newtotal)
