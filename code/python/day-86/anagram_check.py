def Check_Anagram(first_string,second_string):
    first_string = user_input_one.replace(" ","").lower()
    second_string = user_input_two.replace(" ","").lower()
    ascii_of_first_string = 0
    ascii_of_second_string = 0

    for letter in first_string:
        ascii_of_first_string = ascii_of_first_string + ord(letter)

    for letter in second_string:
        ascii_of_second_string = ascii_of_second_string + ord(letter)

    if ascii_of_first_string == ascii_of_second_string:
        print("'{}' and '{}' are anagram.".format(user_input_one,user_input_two))
    else:
        print("'{}' and '{}' are not anagram.".format(user_input_one,user_input_two))

user_input_one = input("Enter a string: ")
user_input_two = input("Enter second string: ")

Check_Anagram(user_input_one,user_input_two)
            
