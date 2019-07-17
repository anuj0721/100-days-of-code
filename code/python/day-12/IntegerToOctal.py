num = int(input("Enter a number: "))
if num==0:
    print(0)
else:
    octal = ''
    while num:
        quest = int(num/8)
        rem = num%8
        octal = str(rem) + octal
        num = quest
    print(octal)
