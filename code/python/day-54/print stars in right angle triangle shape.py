rows = int(input("Enter how many rows?: "))
for row in range(0,rows):
    for col in  range(0,row+1):
        print("*",end="")
    print()
