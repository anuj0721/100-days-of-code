n = int(input("How many even natural numbers you want?: "))

for i in range(1,((2*n)+1)):
    if i%2==0:
        print(i,end=" ")
print()

print("In Reverse Order-")
for i in range(2*n,0,-1):
    if i%2==0:
        print(i,end=" ")
