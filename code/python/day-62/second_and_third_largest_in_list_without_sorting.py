my_list  = [int(num) for num in input("Enter value of list separated by space: ").split()]
if len(my_list) < 5:
    raise ValueError("Please Enter atleast five elements separated by space.")
first_largest = my_list[0]
for value in my_list:
    if value > first_largest:
        first_largest = value
my_list.remove(first_largest)

second_largest = my_list[0]
for value in my_list:
    if value > second_largest:
        second_largest = value
my_list.remove(second_largest)

third_largest = my_list[0]
for value in my_list:
    if value > third_largest:
        third_largest = value

print("Second largest number in given list is {}.".format(second_largest))
print("Third largest number in given list is {}.".format(third_largest))

               

