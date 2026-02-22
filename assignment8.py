# The length of rectangle is 70m and the width is 18m 
# Write a python code that 
# calculate the two times the perimeter of the rectangle and 
# one quarter of the area ,add them and print them out

# solution
length = 70
width = 18
perimeter = 2 * (length+width)
area = length * width 
total = (2 * perimeter)+(area/4)
print(total)