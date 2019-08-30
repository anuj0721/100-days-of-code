rows = int(input("How many rows?: "))
for row in range(rows,0,-1):
    for col in range(0,row):
        print("*",end="")
    print()
