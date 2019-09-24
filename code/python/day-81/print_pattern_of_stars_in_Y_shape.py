rows = int(input("How many rows(Odd and > 1)?: "))
while rows < 3 or rows % 2 == 0:
    print("Number of rows shoud be odd and greater than 1")
    rows = int(input("How many rows(Odd and > 1)?: "))
cols = rows

mid_row = int(rows/2)
mid_col = mid_row

for row in range(0,rows):
    for col in range(0,cols):
        if row == col and row < mid_row:
            print("*",end="")
        elif col == cols - 1 and row < mid_row:
            print("*",end="")
            cols -= 1
        elif row >= mid_row and col == mid_col:
            print("*",end="")
        else:
            print(end=" ")
    print()
