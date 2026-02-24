# Mr James just died and his properties worth $300000, 
# if the children can only inherit 80% of the money and 
# this was divided among his children in the ratio 3:4:5
# However the eldest can only get 70% of his share of the money
# While the youngest can only pick up 50% money too 
# Write a python code that determines
# what the eldest and youngest got finally and  print them out

# Solution
worth = 300000
inherit = (80/100*300000)
print(inherit)
eldest = (5/12*inherit)
print(eldest)
eldestshare = 70/100*eldest
print(eldestshare)
lowest = (3/12*inherit)
lowestshare = 50/100*lowest
print(lowestshare)