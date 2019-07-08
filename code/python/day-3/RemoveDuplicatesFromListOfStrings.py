count = int(input("How many strings you want to enter: "))
strings = []
for i in range(0,count):
    s = input("Enter a string: ")
    strings.append(s)
print("you have entered",strings,"\n")
l = set(strings)
print("New list is",list(l))
    
