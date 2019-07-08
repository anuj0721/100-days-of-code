print("Enter 1 for LCM\nEnter 2 for HCF")
choice = int(input("Enter your choice: "))
if choice == 1:
        def computeLCM(x,y):
                if x>y:
                        greater = x
                else:
                        greater = y
                while (True):
                        if  (greater%x==0) and (greater%y==0):
                                lcm = greater
                                break
                        greater += 1
                return lcm
        
        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))
        print("LCM of",num1,num2,"is",computeLCM(num1,num2))
                
                        
        
elif choice == 2:
        def computeHCF(x,y):
                if x>y:
                        smaller = y
                else:
                        smaller = x
                        
                for i in range(1,smaller+1):
                        if (x%i==0) and (y%i==0):
                                hcf = i
                return hcf
        
        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))
        print("HCF of",num1,num2,"is",computeHCF(num1,num2))

else:
        print("Please Enter correct choice.")
        

                
                
                
