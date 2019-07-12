my_list = [int(x) for x in input("Enter numbers separated by space: ").split()]
 
for i in range(0,len(my_list)):
    if my_list[i]==0:
        print("Yes, a sub array is found with zero sum at index",i)
        exit()
    sum = 0
    for j in range(i,len(my_list)):
        sum = my_list[j]+sum
        if sum == 0:
            print("Yes, A subarray is present with zero sum from index",i,"-",j)
            exit()
   
print("No Subarray is found with zero sum.")
    
 


    
    
    
  
    
