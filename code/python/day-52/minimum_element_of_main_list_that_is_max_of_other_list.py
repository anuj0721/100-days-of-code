main_list = [number for number in input("Enter Main list values separated by space: ").split()]
list_i = int(input("How many other list you want to enter: "))
for value in range(1,list_i+1):
    globals()['my_list%s' %value] = [number for number in input("Enter values separated by space: ").split()]

#find maximum element from all other list.
max_value = int(my_list1[0])   
for i in range(1,list_i+1):
    for value in globals()['my_list%s' %i]:
        if int(value) > max_value:
            max_value = int(value)

#create a list from main_list that contains elements that is greater than from all other list.            
min_list = []
for value in main_list:
    if int(value) > int(max_value):
        min_list.append(value)
# Now find the minimu element in newley created list(it contains elements from main_list that is greater than from all other list.)
min_value = int(min_list[0])
for value in min_list:
    if int(value) < int(min_value):
        min_value = int(value)

print("Minimum number that is greater than all other list, in main list is {}.".format(min_value))

