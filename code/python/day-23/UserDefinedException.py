# pip install colorama
from colorama import Fore, Back
import random
class ValueIsNotNumericError(Exception):
    pass
class ValueIsTooSmallError(Exception):
    pass
class ValueIsTooLargeError(Exception):
    pass

try:
    while True:
        num = input("Guess a number between 1 to 10: ")

        if num.isalpha():
            raise ValueIsNotNumericError
        elif int(num) < 1:
            raise ValueIsTooSmallError
        elif int(num) > 10:
            raise ValueIsTooLargeError
        
        
        res = random.randint(1,10)

        if (int(num)==res):
            print(Fore.YELLOW + Back.BLUE + "Congratulations! You guess it right.")
            break
        else:
            print("Oops! Number was",res)

except ValueIsNotNumericError:
    print("Value is not integer")
except ValueIsTooSmallError:
    print("Value is less than 1")
except ValueIsTooLargeError:
    print("Value is greater than 10")
except:
    print("Something Went wrong! Please enter only integer value between 1-10")
