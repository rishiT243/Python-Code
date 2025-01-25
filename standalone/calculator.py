# Calculator
# we need 2 numbers from the user 
# we need to know what operation to do
# at least 3 variables (all with input)
#casting, convert from one data type to another
# int(),str(),float(convert)
x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
op = input("What operation do you wanna do (+,-, *, /, //, %, **): ")
result = 0

if op == "+":
  result = x + y
elif op == "-":
  result = x-y
elif op == "*":
  result = x*y
elif op == "/":
  result = x/y
elif op == "//":
  result = x//y
elif op == "%":
  result = x%y
elif op == "**":
  result = x**y
else:
  result = "Hey man, that's not an operator, try again"
  
print(result)