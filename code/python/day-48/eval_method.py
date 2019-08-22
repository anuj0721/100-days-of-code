'''The eval function lets a Python program run Python code within itself.
  eval() interprets a string as code.
  eval with input() is a security hole.
  Don't put input() inside an eval statement and you'll be fine'''

num1 = 5
num2 = 6

print(eval("num1 + num2"))
