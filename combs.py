combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y: #  this means is not equal to 
            combs.append((x, y))
        else:
            continue    
print(combs)

combsbasket = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x == y: #  this means is equal to 
            combsbasket.append((x, y))
        else:
            continue    
print(combsbasket)