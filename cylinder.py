# The radius  of a cylinder is 15cm and the height is 25cm.
# calcuate the volume of the cylinder using pyhton code.
# calcuate  the surface area of the cylinder
# add the volume and surface area of the cylinder
#  use  python code
# solution
radius = 15
height = 25
pi = 3.142
volume = pi * radius * radius * height
surfacearea = (2 * pi * radius * radius) + (2 * pi * radius * height)
total = volume + surfacearea
print(total)