# listfruit="orange","orange","orange","apple",
# "apple","apple","apple","apple","apple","banana","pineapple","mango","pawpaw","groundnut"]
# You are given the following list of fruits 
# Write a python code that prints out the list of fruits
# write a python code that removes orange from the list and print the final result.

# Solution
a = "orange"
b = "orange"
c = "orange"
d = "apple"
e = "apple"
f = "apple"
g = "apple"
h = "apple"
i = "apple"
j = "banana"
k = "pineapple"
l = "mango"
m = "pawpaw"
n = "groundnut"
print("This is the list of fruits" , a,b,c,d,e,f,g,h,i,j,k,l,m,n)


fruits = [
    "orange", "orange", "orange",
    "apple", "apple", "apple", "apple", "apple", "apple",
    "banana", "pineapple", "mango", "pawpaw", "groundnut"
]
print("This is the list of fruits:", fruits)
fruits.remove("orange")
print("This is the list of fruits:", fruits)

fruits = [
    "orange", "orange", "orange",
    "apple", "apple", "apple", "apple", "apple", "apple",
    "banana", "pineapple", "mango", "pawpaw", "groundnut"
]

print("This is the list of fruits:", fruits)
fruits.append("orange")
print("This is the list of fruits:", fruits)

for i in fruits:
    print(i)


