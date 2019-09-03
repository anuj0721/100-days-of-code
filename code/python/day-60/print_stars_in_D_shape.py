rows = int(input("How many rows?: "))
if rows <= 0:
    raise ValueError("Rows can not be negative or zero")
cols = int(input("How many columns?: "))
if cols <= 0:
    raise ValueError("Columns can not be negative or zero")

for row in range(0,rows):
    for col in range(0,cols):
        if (((row != 0 and row != rows-1) and (col == 0 or col == cols-1)) or ((row == 0 or row == rows-1) and col < cols-1)):
            print("*",end="")
        else:
            print(end=" ")
    print()
