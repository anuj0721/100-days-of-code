rows = int(input("How many rows?: "))
cols = int(rows/2)+2
for row in range(0,rows):
    for col in range(0,cols):
        if ((row < rows-1) and (col == 0 or col == cols-1)) or ((row == rows-1) and (col > 0 and col < cols-1)):
            print("*",end="")
        else:
            print(end=" ")
    print()
