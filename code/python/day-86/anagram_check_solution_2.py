# Time complexity of this solution - o(n)

def check_anagram(first_string, second_string):
    first_string = first_string.replace(" ","").lower()
    second_string = second_string.replace(" ","").lower()

    #Edge case check
    if len(first_string) != len(second_string):
        print("'{}' and '{}' are not anagram.".format(first_string, second_string))
    else:

        count = {}

        for letter in first_string:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1

        for letter in second_string:
            if letter in count:
                count[letter] -= 1
            else:
                count[letter] = 1

        for k in count:
            if count[k] != 0:
                print("'{}' and '{}' are not anagram.".format(first_string, second_string))
                break
        else:
            print("'{}' and '{}' are anagram.".format(first_string, second_string))

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
check_anagram(s1,s2)
            
