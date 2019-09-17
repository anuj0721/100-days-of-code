def reverse_string(curr_string):
    curr_string = curr_string.replace(" ","")
    print(curr_string[::-1])
    
user_input = input("Enter a string: ")
reverse_string(user_input)

