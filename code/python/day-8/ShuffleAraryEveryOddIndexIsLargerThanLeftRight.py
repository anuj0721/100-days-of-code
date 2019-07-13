user_input = [int(x) for x in input("Enter Unique values separated by space: ").split()]
s = set(user_input) #to sort the array and remove duplicates
a = list(s)

ans = [0]*len(a)
p = 0
q = len(a)-1

for i in range(len(a)):
    if (i+1)%2==0:  #Assign Even Indexes to maximum elements 
        ans[i] = a[q]
        q = q-1
    else:           #Assign odd indexes to remaining elements
        ans[i] = a[p]
        p = p+1
print("Reshuffled List is:",ans)
