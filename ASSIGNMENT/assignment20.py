# The length of a house is 42m and the breath is 34m
# write a python code that will calculate the perimeter and the area 
# (separately)
# Then add the 1/3 of the perimeter and double the area together and 
# print out the final results
#Formula: area = length *breadth #Perimeter = (length +breadth)*2

# Solution
length = 42
breadth = 34
perimeter = (length + breadth)*2
print(perimeter)
area = length *breadth
print(area)
newresult = (perimeter*1/3)+(2*area)
print(newresult)
