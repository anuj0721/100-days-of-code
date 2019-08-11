def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)
def factt(s):
    if s == 1:
        return s
    else:
        return s*factt(s-1)
num = int(input("Enter a number: "))
samp = int(input("Enter Sample points in each combination: "))
sum = num-samp

permutation = fact(num)/factt(sum)
permutation = int(permutation)
print("permutation is {}".format(permutation))

if permutation/8==0:
    print("Permutation is divided by 8")
else:
    print("Permutation is not divided by 8")




