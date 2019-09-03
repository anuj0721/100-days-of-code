x,y = 0,0
while x == 0 or y == 0 or x < 0 or y < 0: 
    x,y = [int(num) for num in input("Enter Positive Integer value of x and y separated by space: ").split()]
    
power_num = pow(x,y) 

last_digit = power_num % 10

print("Last Digit of {}^{} is {}".format(x,y,last_digit))
