rows = int(input("How many rows?: "))
if rows <= 0:
    raise ValueError("No of rows can not be zero or negative.")
cols = int(input("How many columns?: "))
if cols <= 0:
    raise ValueError("No of columns can not be zero or negative")

mid_row = int(rows/2)

for row in range(0,rows):
    for col in range(0,cols):
        if (col == 0) or ((row == 0 or row == mid_row or row == rows-1) and (col > 0)) :
            print("*",end="")
    print()
