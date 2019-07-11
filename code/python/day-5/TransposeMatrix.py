n = int(input("How many rows and columns?: "))
m = n #number of rows and columns are same

mat = [[0]*m for i in range(n)]

#iterate through columns
for i in range(n):
    for j in range(m):
        print("Enter value row wise",i,j)
        mat[i][j]=int(input())
for row in mat:
    print(row)

print("Transposed Matrix is:")

#iterate through rows
res = [[mat[i][j] for i in range(m)] for j in range(n)]
for row in res:
    print(row)
