rows = int(input("How many rows?: "))
cols = rows-2
mid_row = int(rows/2)
for row in range(0,rows):
    for col in range(0,cols):
        if ((col == 0) or ((row > 0 and row < mid_row) and (col == cols-1)) or ((row == 0 or row == mid_row) and (col > 0 and col < cols-1)) or ((row == mid_row+col) and (col > 0))):
            print("*",end="")
        else:
            print(end=" ")
    print()

