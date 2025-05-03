# x =5
# b = 10
# calc = f"({x} + {b} )/ 2"

# mini langauge
# able to save variables
# able to do calculations
# print variables
variables = {}
while True:
    text = """Options: 
    1. make new variable
    2. update a variable
    3. see all variables
    4. do calculation with variables"""
    print(text)
    menu = input("Enter your choice: ")
    if menu == "1":
        while True:
            name = input("What is the variable name: ")
            if name.isalpha():
                if variables.get(name) == None:
                    data = input("What does it represent: ")
                    variables.update({name:data})
                    print("Variable added")
                    break
                else:
                    print("Variable already exists")
                    break
            else:
                continue

    elif menu == "2":
        name = input("What variable do you want to update: ")
        if variables.get(name) != None:
            data = input("What do you want to update it with: ")
            variables.update({name:data})
    elif menu == "3":
        for variable in variables:
            print(f"{variable} = {variables[variable]}")
    elif menu == "4":
        operators = "+,-,/,*,**,//,%"
        print(f"available operations: {operators}")
        op = input("What operation would you like to perform: ")
        var1 = input("What is the first variable: ")
        var2 = input("What is the second variable: ")
        var1Data = variables.get(var1)
        var2Data = variables.get(var2)
        print(f"{var1} {op} {var2}")
        print(eval(f"{var1Data} {op} {var2Data}"))
        



# print(eval(calc))
operators = ["+","-","/","*","**","//","%"]
while True:
    try:
        calc = input("What is an expression you want to know the answer to?: ")
        print(eval(calc))
    except NameError:
        print("NameError")
    except SyntaxError:
        print("SyntaxError")
    except KeyboardInterrupt:
        print("\nGoodbye")
        break
