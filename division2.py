a = 109
b = 209
c = 309
d = a*b*c/10-500
print("this is the result  of task, d")
if d < 10000:
    print("yes it is less than 10000")
    e = d/3
    print(e)
else:
    print("no it is greater than 10000")
    e = d + 5000
    print(e)