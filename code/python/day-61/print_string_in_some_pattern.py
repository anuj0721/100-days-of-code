user_input = input("Enter a string without space: ")
if user_input.isalpha():
    string = user_input.lower()
    for char in range(0,len(string)):
        if char == 0:
            print("{}-".format(string[char].upper()),end="")
        else:
            for m in range(0,char+1):
                if m == 0:
                    print(string[char].upper(),end="")
                else:
                    print(string[char],end="")
                if m == len(string) - 1:
                    exit()
            print("-",end="")
else:
    print("Please enter only alphabets.")
