rows = int(input("How many rows:? "))
cols = (rows*2)-1
for row in range(0,rows):
    for col in range(0,cols):
        if col == row:
            print("*",end="")
        elif col == cols-1:
            while row < rows-1:
                print("*",end="")
                cols -= 1
                break
        else:
            print(end=" ")
    print()
