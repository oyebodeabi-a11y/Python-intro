# mr john took a loan of principal 500k for two years at the rate of 5%
# and mrs bukola took another loan of principal 900,000 for 3 years at the rate of 5%
# write a python code that will calculate each individual simple interest.
# once you get that pls add the simple interest together but you must display (print) only 75%
# Formula: SI=PTR/100

# Solution
loan1 = 500000
t1 = 2
r1 = 5/100
loan2 = 900000
t2 = 3
r2 = 5/100
totalsi = (loan1*2*r1)/100+(loan2*3*r2)/100
print(totalsi)
newtotalsi = totalsi/((loan1*2*r1)/100+(loan2*3*r2)/100)*100
print(newtotalsi)