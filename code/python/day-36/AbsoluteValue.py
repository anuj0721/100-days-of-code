num = input("Enter a number to get absolute value: ")
try:
    if num.isalpha():
        print("Please Enter only numerical or complex value.")
    elif num.isnumeric():
        absvalue = abs(int(num))
        print("Absolute Value of {} is".format(num),absvalue)
    else:
        try:
            num = float(num)
            absvalue = abs(num)
            print("Absolute Value of {} is".format(num),absvalue)
        except:
            num = num.replace(" ","")
            num = complex(num)
            absvalue = abs(num)
            print("Absolute Value of {} is".format(num),absvalue)
except:
    print("Something Went Wrong! Please Try Again.")
