from functools import reduce
import operator

def add(num):
    s = 0
    for i in num:
        s = int(s)+int(i)
    print(s)

def mul(num):
    s = 1
    for i in num:
        s = int(s)*int(i)
    print(s)

def sub(num):
    s = reduce(operator.__sub__, num)
    print(s)
    
def div(num):
    s = reduce(operator.__truediv__,num)
    print(s)
print("Enter:")    
print("1 for Addition\n2 for Multiplication\n3 for subtraction\n4 for divide")
choice = int(input("Enter your choice: "))

if (choice==1):
    num = [int(x) for x in input("Enter values separated by space for addition: ").split()]
    add(num)
elif (choice==2):
    num = [int(x) for x in input("Enter values separated by space to multiply:").split()]
    mul(num)
elif (choice==3):
    num = [int(x) for x in input("Enter values separated by space to subtract:").split()]
    sub(num)
elif (choice==4):
    num = [int(x) for x in input("Enter values separated by space for division:").split()]
    div(num)
else:
    print("Please enter correct choice!")
