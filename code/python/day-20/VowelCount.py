string = input("Enter a string of alphabets: ")
vowels = ['A','E','I','O','U','a','e','i','o','u']
if string.isalpha():
    count = 0
    for v in string:
        if v in vowels:
            count = count+1
    print(count,"vowels are present in",string)
else:
    raise ValueError("Please Enter only alphabets")
    

    
