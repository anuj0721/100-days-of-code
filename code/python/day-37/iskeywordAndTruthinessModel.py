# Everything in python is an object.
# == used to check the value of object.
# 'is' keyword check the identity(Address of the memory) of object.

L1 = [1,2,3,4]
L2 = [1,2,3,4]

if L1 == L2:
    print(" == executed")

if L1 is L2:
    print("is keyword executed")


print("Id of L1 is",id(L1))
print("Id of L2 is",id(L2))

#python truthiness model
# if a value is non zero then python consider it true.
# same for containers like list/tuple/dict..
# ..if container is non empty then python cosiders it true.

a = 0
if (a):
    print("It will return false because value of a is 0")

a = 2
b = -5

if a and b:
    print("It will return true because value of a and b is non-zero")

a = 0
if not a: #this conditon will be true becaue value of a is not non-zero
    a = int(input("Enter value of a: "))
    if a:
        print("Value of a is",a,"That is non zero")
    else:
        print("You entered zero")
