def kmtomiles(k):
        ml = k/1.609
        print("{0: .2f}".format(ml),"miles")

def milestokm(m):
    km = m*1.609
    print("{0: .2f}".format(km),"kms")
    
while True:
    ln = input("Enter Length: ")
    try:
        ln = float(ln)
    
        print("Enter 1 to convert km to miles. \nEnter 2 to convert miles to km.")
        while True:
            choice = input("Enter your choice: ")
            if choice == "1":
                kmtomiles(ln)
                break
            elif choice == "2":
                milestokm(ln)
                break
            else:
                print("Please Enter either 1 or 2")
        break

    except:
        print("Please Enter only numerical value.")
