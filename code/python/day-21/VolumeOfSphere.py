try:
    radius = float(input("Enter radius of sphere: "))
    volume = ((4/3)*(3.14)*(pow(radius,3)))
    print("Volume of shpere is",volume,"meter cube")
except ValueError:
    print("Please enter only numeric value")
finally:
    print("Program is executed.")
    
