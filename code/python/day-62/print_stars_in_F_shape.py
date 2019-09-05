rows = int(input("Enter number of rows?: "))
mid_row = int(rows/2)
cols = int(input("Enter number of columns?: "))
for row in range(0,rows):
    for col in range(0,cols):
        if ((col == 0) or ((row == 0 or row == mid_row) and (col > 0))):
            print("*",end="")
    print()
