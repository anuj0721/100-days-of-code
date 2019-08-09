def countcaseofstring(s):
    lcount = 0
    ucount = 0

    choice = input("Do you want to use inbuilt function islower()? Enter:y/n: ")

    if choice == "y":

        for i in s:
            if i.islower():
                lcount += 1
            else:
                ucount += 1
        print("There are",ucount,"Upppercase and",lcount,"lowercase letters.")

    elif choice == "n":
    
        L = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        for i in s:
            if i in L:
                ucount += 1
            else:
                lcount += 1

        print("There are",ucount,"Upppercase and",lcount,"lowercase letters.")

    else:
        print("Please Enter only y/n: ",end="")
        countcaseofstring(string)


while True:
    string = str(input("Enter an alphabetic string: "))
    string  = string.replace(" ","")
    if string.isalpha():
        countcaseofstring(string)
        break
    else:
        print("You entered an non alphabetic string!")
