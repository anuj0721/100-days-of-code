rows = int(input("How many rows? "))
space = rows-1
for row in range(0,rows):
    for col in range(0,space):
        print(end="  ")
    for col in range(row+1,0,-1):
        print(col,end=" ")
    i = 2
    for col in range(0,row):
        print(i,end=" ")
        i += 1
        

    print()
    space -= 1
