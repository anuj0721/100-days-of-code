rows = int(input("How many rows?: "))
k = 0
for row in range(rows,0,-1):
    for col in range(0,k):
        print(end=" ")
    for col in range(0,row):
        print("*",end=" ")
    print()
    k += 1
