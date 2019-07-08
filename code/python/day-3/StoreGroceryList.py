n = int(input("How many entries: "))
GroceryName = []
GroceryQty = []
for i in range(0,n):
    GName = input("Enter Grocery Name: ")
    GroceryName.append(GName)
for i in range(0,n):
    GQty = input("Enter Quantity: ")
    GroceryQty.append(GQty)
d = dict(zip(GroceryName,GroceryQty))

with open("Grocerylist.txt","w") as f:
    f.write(str(d))
    
print("Text File written successfully!\nNow Reading File...")
f = open("Grocerylist.txt","r")
showdict = eval(f.read())
print(showdict)
f.close()



