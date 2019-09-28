rows = int(input("How many rows?: "))
if rows > 9:
    print("Maximum rows can be 9.\nFor dynamic input further part has not been developed yet.")
else:
    space = rows-1
    for row in range(0, rows):
        i = 1
        for col in range(0, space):
            print(end="  ")
        for col in range(0, row+1):
            print(i, end=" ")
            i += 1
        for col in range(row, 0, -1):
            print(col, end=" ")
        print()
        space -= 1
