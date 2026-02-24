# mrs yinka monthly upkeep budget given by her husband is #250,000
# she was meticulous enough to buy the following items
# 4 tubers of yam@ #500 each,bought three stationeries@ #2000 each
# pays debt of 45,000,pays shop deal of 25k monthly for three months due
# Write python code that determines how much she has left from the budget

# solution
money = 250000
yam = 4*500
stationery = 3*2000
debt = 45000
shop = 3*25000
balance = money - (yam+stationery+debt+shop)
print("this is the balance amount:",balance)