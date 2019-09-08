rows = int(input("How many rows?:"))
cols = int(input("How many columns(Odd)?: "))
mid_col = int(cols/2)
for row in range(0,rows):
    for col in range(0,cols):
        if ((row == 0 or row == rows-1) or ((col == mid_col) and (row > 0 and row < rows - 1))):
            print("*",end="")
        else:
            print(end=" ")
    print()
