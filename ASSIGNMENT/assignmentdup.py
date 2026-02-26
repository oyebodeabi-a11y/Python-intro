# to check for duplicate item and print them out ignore the extensions
listme1=["orange.txt","yam.txt","chiz.mb","chiz.mb","chiz.mb","chiz.mb",
         "pineapple.jpg","pineapple.jpg","pineapple.jpg","mango.mb","pawpaw.doc","groundnut.jpg"]
opt=[]
duplicateitem=[]

for item in listme1:
    opt.append(item)
    if opt.count(item)>1:
       
        duplicateitem.append(item)
    else:
        continue       
print("This is the list of duplicated items:" ,duplicateitem)