my_list = [int(num) for num in input("Enter values of list separated by space: ").split()]
if len(my_list) < 5:
    raise ValueError("Please Enter atleast five elements separated by space.")

largest = 0
second_largest = 0
third_largest = 0

for value in my_list:

    # assign the new largest, and push the rest of them back down the chain
    # we use >= instead of > to ensure that duplicate maximums still work.
    
    if value >= largest:
        largest,second_largest,third_largest = value,largest,second_largest
    elif value >= second_largest:
        second_largest,third_largest = value,second_largest
    elif value >= third_largest:
        third_largest = value

print("Second largest number in given list is {}".format(second_largest))
print("Third largest number in given list is {}".format(third_largest))

