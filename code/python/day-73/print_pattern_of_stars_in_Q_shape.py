rows = int(input("How many rows:? "))
if rows < 7:
    raise ValueError("No of rows must be greater than 6")
cols = rows-3
for row in range(1,rows+1):
    for col in range(1,cols+1):
        if (row > 1 and row < rows-1) and (col == 1 or col == cols) or (row == 1 or row == rows-1) and (col > 1 and col < cols) or (row == rows and col == cols-1) or (row == rows-2 and col == cols-3):
            print("*",end="")
        else:
            print(end=" ")
    print()

print()

