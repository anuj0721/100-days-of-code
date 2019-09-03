rows, cols = 0,0
try:
    while rows <= 0:
        rows = int(input("How many rows? "))
        if rows <= 0:
            print("Plase Enter only non zero positive integer value")
    while cols <= 0:
        cols = int(input("How many columns?: "))
        if cols <= 0:
            print("Plase Enter only non zero positive integer value")
except:
    print("Please Enter only non-zero positive integer")

for row in range(0,rows):
    for col in range(0,cols):
        if col == 0 or (col > 0 and row == 0 or row == rows-1):
            print("*",end="")
    print()
    
