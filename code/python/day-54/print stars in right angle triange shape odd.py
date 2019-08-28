rows = int(input("Enter how many rows?: "))
k = 1
for row in range(0,rows):
    for col in range(0,row+k):
        print("*",end="")
    k += 1
    print()
    
