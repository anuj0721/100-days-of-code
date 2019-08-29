rows = int(input("How many rows?: "))
k = rows-1
for row in range(0,rows):
    for col in range(k,0,-1):
        print(end=" ")
    for col in range(0,row+1):
        print("*",end=" ")
    print()
    k -= 1
