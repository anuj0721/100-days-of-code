my_list = [int(num) for num in input("Enter values separated by space: ").split()]
my_list.sort()
largest = my_list[len(my_list)-1]
second_largest = my_list[len(my_list)-2]
smallest = my_list[0]
second_smallest = my_list[1]

print("Largest value in given list is {}".format(largest))
print("Smallest value in given list is {}".format(smallest))
print("Second largest value in given list is {}".format(second_largest))
print("Second smallest value in given list is {}".format(second_smallest))
