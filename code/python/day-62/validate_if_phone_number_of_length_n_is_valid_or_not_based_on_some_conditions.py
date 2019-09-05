def Validate(num):
    flag = True
    for value in num:
        if value == '7' or value == '2' or value == '9':
            flag = False

    if flag == True:    
        i = 1
        for value in range(0,len(num)-1):
            if num[value] == num[value+1]:
                flag = False
            i += 1

    if flag == True:
        if '4' in num:
            if num[0] == '4':
                print("valid")
                quit()
            else:
                print("invalid")
                quit()
        else:
            print("valid")

    elif flag == False:
        print("invalid")

phone_number = input("Enter a phone number: ")
Validate(phone_number)
        
    
