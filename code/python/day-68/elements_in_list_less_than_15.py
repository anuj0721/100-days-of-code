try:
    my_list = [int(num) for num in input("Enter values of list separated by space: ").split()]
except:
    raise ValueError("Please Enter only numerical value")
    
filtered_list = list(filter(lambda x: (x < 15),my_list))
print("Elements that are less than 15 in given list is-")
filtered_list.sort()
for value in filtered_list:
    print(value)
