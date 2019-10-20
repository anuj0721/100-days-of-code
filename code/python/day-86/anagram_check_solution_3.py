def anagram_check(first_string, second_string):
    first_string = first_string.replace(" ","").lower()
    second_string = second_string.replace(" ","").lower()

    if sorted(first_string) == sorted(second_string):
        print("'{}' and '{}' are anagram.".format(first_string, second_string))
    else:
        print("'{}' and '{}' are not anagram.".format(first_string, second_string))

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
anagram_check(s1,s2)
