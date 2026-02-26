# How many times is Yes present in the statement below:

animal=["Yes",  "Yes", "Yes", "No","Yes", 
        "Yes", "Yes","Yes","Yes", "No",
        "Yes", "No", "Yes", "No",   "No", 
        "Yes","Yes", "Yes", "Yes", "Yes",
        "No",  "No",  "Yes","Yes", "No",
        "Yes"]

counter=0
animalspresent=[]

for i in animal:
    if i =="Yes": #meaning present
        counter=counter=+1
        
        animalspresent.append(i)
            
    else:
        continue

print(animalspresent.count(i)) 
    
 # call the function for the final outcome

nocounter=0
absent=[]
for item in animal:
    if item =="No": #meaning present
        print(item)
        nocounter=nocounter+1
        print(nocounter)
        absent.append(item)           
    else:
        continue 
print(absent.count(item))
print("This is the absent animals",len(absent))