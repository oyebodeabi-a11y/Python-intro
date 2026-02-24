#  Different exercise on list
# listfruit="orange","orange","orange","apple",
# "apple","apple","apple","apple","apple","banana","pineapple","mango","pawpaw","groundnut"]
# You are given the following list of fruits 
# Write a python code that prints out the list of fruits
# write a python code that removes orange from the list and print the final result.
# Write a python code to add orange to the list and print the final  outcome

# Solution
fruits = [
    "orange", "orange", "orange",
    "apple", "apple", "apple", "apple", "apple", "apple",
    "banana", "pineapple", "mango", "pawpaw", "groundnut"
]

#print("This is the list of fruits:", fruits)
#fruits.append("orange")
#print("This is the list of fruits:", fruits)

basket = []
for i in fruits:
    # print(i)
    if i == "apple":    
          #print(i)
          basket.append(i)
    else:
        continue
basket.append("mango")
basket.append("groundnut")
basket.append("pineapple")
print(basket)
basket.remove("pineapple")
#if basket.count("pineapple")>1:
    #basket.remove("pineappple")
print(basket)
print("Total items in basket:", len(basket))


