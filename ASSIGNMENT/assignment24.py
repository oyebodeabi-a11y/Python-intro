# Mr James just died and his properties worth $58000 
# but he owe a debt of $10000, 
# the balance was among his children in the ratio 1:2:3
# Write a python code that determines 
# who got the highest and lowest and print them out

#solution
properties = 58000
debt = 10000
balance = properties - debt
print(balance)
highestbalance = balance*3/6
print(highestbalance)
lowestbalance = balance*1/6
print(lowestbalance)
