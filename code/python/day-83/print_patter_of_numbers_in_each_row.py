rows = int(input("How many rows?"))
for row in range(0, rows):
    i = 1
    for col in range(0, row+1):
        print(i, end="")
        i += 1
    print()
