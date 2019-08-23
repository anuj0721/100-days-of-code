my_list = [number for number in input("Enter integers value separated by space: ").split(" ")]
my_set = set(my_list)
pair = 0
for value in my_set:
    if my_list.count(value) > 1:
        total = my_list.count(value)
        total = int((total/2))
        pair += total

print("{} pair exist.".format(pair))


        
        
        
        

