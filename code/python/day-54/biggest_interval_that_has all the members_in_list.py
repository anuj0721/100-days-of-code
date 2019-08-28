my_list = [int(number) for number in input("Enter values separated by space: ").split(" ")]
my_list.sort()
max_interval = 2*[0]
min_count = None

'''Iterate over the list and if both elements are same then skip'''
for value in range(0,len(my_list)):
    for jvalue in range(0,len(my_list)):
        if my_list[value] == my_list[jvalue]:
            continue

        '''Generate a temerary list that contains all elements between
            two values of given list including self'''
        temp = []
        for num in range(my_list[value],my_list[jvalue]+1):
            temp.append(num)

        '''Check if temperary list contains all elements of given list'''

        is_contain = all(item in my_list for item in temp)

        curr_count = len(temp) # count the length of temerary list.

        if is_contain == True and curr_count>0: '''this condition will be true 
                                                    only when temperaty list contains
                                                    all elements of given list.'''


.            ''''below condtion will ensure that temprary list will be of
                maximum length. because maximum length of temp list will give
                us the biggest interval(distance) between values of given list.'''
            if (min_count is None) or curr_count > min_count:
                min_count = curr_count
                max_interval[0] = my_list[value]
                max_interval[1] = my_list[jvalue]

print(max_interval)
