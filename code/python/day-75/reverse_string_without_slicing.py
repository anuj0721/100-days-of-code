def reverse_string(curr_string):
    for char in range(len(curr_string)-1,-1,-1):
        print(curr_string[char],end="")
user_input = input("Enter a string: ")
reverse_string(user_input)


