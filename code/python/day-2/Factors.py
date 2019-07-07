def Factor(n):
    if n==0:
        return "0 has infinite number of factors which include all whole numbers."
    elif n==1:
        return "Factor of 1 is 1"
    else:
        f = []
        for i in range(1,n+1):
            if n%i == 0:
                f.append(i)
        print("Factors of",n,"is",end=" ")
        return f   

num = int(input("Enter a positive whole number to get Factors: "))
res = Factor(num)
print(res)
