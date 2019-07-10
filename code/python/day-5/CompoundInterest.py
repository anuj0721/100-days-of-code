p = float(input("Enter Prinicpal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))
rate = (100+r)/100
cinterest = (p * pow(rate,t))-p
print("Compound Interes is",cinterest)
