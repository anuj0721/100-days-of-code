try:
    s = int(input("Enter starting range: "))
    e = int(input("Enter ending range: "))
    for i in range(s,e+1):
        for j in range(1,11):
            res = i*j
            print(res,end="\t")
        print()
except ValueError:
    print("Please Enter only integer value")
        
