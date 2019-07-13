import random
while True:
    addx = random.randint(1,100)
    addy = random.randint(1,100)
    print(addx,"+",addy,"=",end=" ")
    add = int(input())
    addres = addx + addy
    if add == addres:
        print("Correct")
    else:
        print("Wrong")
    subx = random.randint(1,100)
    suby = random.randint(1,100)
    print(subx,"-",suby,"=",end=" ")
    sub = int(input())
    subres = subx - suby
    if sub == subres:
        print("Correct")
    else:
        print("wrong")
