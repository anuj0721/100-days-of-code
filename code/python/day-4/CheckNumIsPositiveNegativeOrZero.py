try:
    def checknum(num):
        if num == float(num):
            if num<0:
                print(num,"is negative number.")
            elif num==0:
                print("You Entered Zero.")
            elif num>0:
                print(num,"Positive number.")
            
    user_input = float(input("Enter a numeric value: "))
    checknum(user_input)

except:
    print("Thats not a number.\n")
    user_input = float(input("Please Enter only a numeric value: "))
    checknum(user_input)


        
