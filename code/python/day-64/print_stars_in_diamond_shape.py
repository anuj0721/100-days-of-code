user_input = int(input("How many rows? "))
rows = (int(user_input/2)) + 1 
k = rows-1
for row in range(0,rows):
    for col in range(k,0,-1):
        print(end=" ")
    for col in range(0,row+1):
        print("*",end=" ")
    print()
    k -= 1

rows = int(user_input/2)
k = 1
for row in range(rows,0,-1):
    for col in range(0,k):
        print(end=" ")
    for col in range(0,row):
        print("*",end=" ")
    print()
    k += 1
