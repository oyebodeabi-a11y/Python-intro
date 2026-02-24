# Mr Thomas has four properties valued at 100,000 each
# his father gave him 50,000
# his mum gave him 150,000
# He bought a car at a value of 200,000
# he gave his wife 30000,
# if the money in his account initially was 300,000 
# but he can only spend 3/4 of the money
#Write a python code that will show how much he has in his account

# solution 
Money1 = 300000
house = 100000*4
gift1 = 50000
gift2 = 150000
car = 200000
wife = 30000
moneyhad = (house+gift1+gift2)
print(moneyhad)
moneyspent = car+wife
accountspend = (Money1*3/4)
print(accountspend)
moneymade = moneyhad - moneyspent
print(moneymade)
newmoney = accountspend+moneymade
print(newmoney)
