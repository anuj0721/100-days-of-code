my_list = [int(x) for x in input("Enter values separated by space: ").split()]
maxm = 0
for i in range(0,len(my_list)):
    for j in range(0,len(my_list)):
        if my_list[i] == my_list[j]:
            continue
        prod = my_list[i]*my_list[j]
        if prod > maxm:
            maxm = prod
            first = my_list[i]
            second = my_list[j]
print("Largest product is",maxm,"at pair(",first,second,")")
    
