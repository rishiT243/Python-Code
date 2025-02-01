# Calculator
# we need 2 numbers from the user 
# we need to know what operation to do
# at least 3 variables (all with input)
#casting, convert from one data type to another
# int(),str(),float(convert)

#taking in input




quit = False
history = []
ans = 0
#name.append(thing)
#name.remove(thing)
while not quit:
  q = input("Would you like to use the calculator? (y/n): ")
  if q == "n":
    print("goodbye")
    quit = True
    continue
  elif q == "y":
    if len(history) > 0:
      ans = history[len(history)-1]
    print(f"History: {history}")
    x = input("Enter your first number: ")
    if x == "ans":
      x = ans
    else:
      x = int(x)
    y = input("Enter your second number: ")
    if y == "ans":
      y = ans
    else:
      y = int(y)
    op = input("What operation do you wanna do (+,-, *, /, //, %, **): ")
    result = 0

    # operations
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
    
    if result != "Hey man, that's not an operator, try again":
      history.append(result)
    print(result)
  else:
    print("Please enter y or n")


