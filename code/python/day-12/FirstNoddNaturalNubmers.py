n = int(input("How many odd natural numbers you want?: "))
for i in range(1,((2*n)+1)):
    if i%2!=0:
        print(i,end=" ")
