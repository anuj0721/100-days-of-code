rows = int(input("How many rows?: "))
cols = 4
for row in range(0,rows):
    for col in range(0,cols):
        if ((row != 0 and col == 1) or (row == 0 and col != 1)):
            print("*",end="")
        else:
            print(end=" ")
    print()

