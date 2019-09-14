rows = int(input("How many rows?: "))
if rows < 5:
    raise ValueError("Rows should be atleast 5")
cols = rows-2
for row in range(0,rows):
    for col in range(0,cols):
        if (((row > 0 and row < rows-1) and (col == 0 or col == cols-1)) or ((row == 0 or row == rows-1) and (col > 0 and col < cols-1))):
            print("*",end="")
        else:
            print(end=" ")
    print()
