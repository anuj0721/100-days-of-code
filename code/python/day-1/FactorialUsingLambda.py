fact = lambda n: 1 if n==1 or n==0 else ("Factorial for negative number does not exist." if n<0 else n*fact (n-1))
num = int(input("Enter a number: "))
print(fact(num))
          
