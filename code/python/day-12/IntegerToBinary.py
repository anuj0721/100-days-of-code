num = int(input("Enter a number: "))
if num==0:
    print(0)
else:
    binary = ''
    while num:
        quest = int(num/2)
        rem = num%2
        binary = str(rem) + binary
        num = quest
    print(binary)
    
    
