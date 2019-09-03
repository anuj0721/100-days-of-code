my_list = [int(num) for num in input("Enter integer values separated by space.").split()]
total_sum = 0
for value in range(0,len(my_list)):
    total_sum = total_sum + my_list[value]

first_digit = total_sum

while first_digit >= 10:
    first_digit = int(first_digit/10)

print("First Digit of sum of list is {}".format(first_digit))
