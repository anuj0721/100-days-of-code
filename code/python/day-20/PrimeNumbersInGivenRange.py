start = int(input("Enter starting range?: "))
end = int(input("Enter ending range?: "))
if start<=1:
    start=2  
prime = []
for i in range(start,end+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        prime.append(i)
print(prime)

