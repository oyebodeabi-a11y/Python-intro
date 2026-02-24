# Mrs Bridget went to market she bought the following items from the market:
#Pawpaw 200 pieces @50 per one
#Ginger. 500 @5 each
#Groundnut 100 @10 each
#Stationeries 350 @ 10 per one
#Stationeries 650 @ 10 per one
#Bread for the kids 10 loaves @ 100 each
# If she had 10,000 in her account but she can only spend 75% of this amount 
# nothingmore
# Now the question:Write python code that determines 
# how much does mrs Bridget has left off the 75%

# Solution:
pawpaw = 200*50
ginger = 500*5
groundnut = 100*10
stationeries1 = 350*10
stationeries2 = 650*10
bread = 100*10
spent = (pawpaw+ginger+groundnut+stationeries1+stationeries2+bread)
print(spent)
accmoney = 10000*75/100
print(accmoney)
balance = accmoney - (pawpaw+ginger+groundnut+stationeries1+stationeries2+bread)
print(balance)