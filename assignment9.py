# The radius of circle is 10cm, if pie =3.142.
# Write a python code that will calculate 
# the double the area of the circle and 
# the one third of the circumference of the circle. 
# Add the two results together and print it out

# solution
radius = 10
pi = 3.142
area = pi*radius*radius
circumference = 2*pi*radius
total = (2*area)+(circumference/3)
print(total)