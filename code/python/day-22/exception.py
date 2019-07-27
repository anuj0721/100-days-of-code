# Exception is an unexpected or unwanted event that occours during the execution of the program
# and disrupts the normal flow of program instructions.
# So to maintain the normal flow of program we do exception handling.

try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    z = a/b
    print(z)
    if isinstance(z,float):
        raise Warning("Answer in float")
except ZeroDivisionError:
    print("you divided by 0")
except ValueError:
    print("Please Enter only integer value.")
finally:
    print("Program executed.")


    # defining your own exceptions

    class MyError(Exception):
        print("This is a problem")

    raise MyError("MyError Occurred")

    assert(1==0) # it's a debugging aid that tests a condition.
                 # if contdion is true it does nothing.
                 # if false it raise an AssertionError Exception.
