rows = int(input("How many rows?: "))
cols = int(input("How many columns?: "))
for row in range(0,rows):
    for col in range(0,cols):
        if (col == 0) or (row == rows-1 and col > 0):
            print("*",end="")
    print()
