rows = int(input("How many rows(Enter odd number)?: "))
rows = int((rows+1)/2)
k = rows-1
for row in range(0,rows):
    for col in range(k,0,-1):
        print(end=" ")
    for col in range(0,row+1):
        print("*",end=" ")
    k -= 1
    print()

k = 1
for row in range(rows-1,0,-1):
    for col in range(0,k):
        print(end=" ")
    for col in range(0,row):
        print("*",end=" ")
    k += 1
    print()
        
    
