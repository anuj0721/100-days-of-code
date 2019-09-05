my_list = [int(num) for num in input("Enter elements of list separated by space: ").split()]

largest = max(my_list)
my_list.remove(largest)

second_largest = max(my_list)
my_list.remove(second_largest)

third_largest = max(my_list)

print("Second largest number in given list is {}".format(second_largest))
print("Third largest number in given list is {}".format(third_largest))
