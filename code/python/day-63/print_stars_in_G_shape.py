rows = int(input("How many rows?: "))
cols = int(input("How many columns?: "))
mid_row = (int(rows/2))
mid_col = (int(cols/2))
for row in range(0,rows):
    for col in range(0,cols):
        if ((col == 0) or ((row == 0 or row == rows-1) and (col > 0 and col <= mid_col)) or ((row == mid_row or row == rows-1) and (col > mid_col)) or ((row > mid_row and row < rows-1) and (col == cols-1))):
            print("*",end="")
        else:
            print(end=" ")
    print()
