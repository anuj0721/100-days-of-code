n = int(input("Enter a number to get factorial: "))
if (n<0):
    print("Factorial of negative numbers does not exist.")
elif (n==0):
    print("Factorial of 0 is 1")
else:
    fact = 1
    for i in range(1,n+1):
        fact = i*fact
    print(fact)        
