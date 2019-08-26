my_list = [number for number in input("Enter values separated by space: ").split()]
min_value = my_list[0]
for value in my_list:
    if int(value) < int(min_value):
        min_value = value
print("Minimum Value in list is {}.".format(min_value))
    
