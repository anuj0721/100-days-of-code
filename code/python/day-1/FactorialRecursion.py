def fact(n):
    if (n < 0):
        return "not available/exist."
    elif (n == 1 or n == 0):
        return 1
    else:
        return n*fact(n-1)
    
num = int(input("Enter a number: "))
f = fact(num)
print("factorial of",num,"is ",f)

    
