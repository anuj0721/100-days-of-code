total = 0
count = 0
my_list = [number for number in input("Enter a list of integers.").split(" ")]
sorted_list = sorted(my_list)
my_set = set(sorted_list)
sorted_set = sorted(my_set)
unique_list = list(sorted_set)

for self in unique_list:
    total += 1

for value in range(0,len(sorted_set)):
    for jvalue in range(0,len(sorted_list)):
        if unique_list[value] == my_list[jvalue]:
            count += 1

pairs = int((count-total)/2)
print("{} pair exist.".format(pairs))    
