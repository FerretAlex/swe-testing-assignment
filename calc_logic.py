def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error"
    else:
        return a / b

def clear():
    return 0

# Testing
#print("Type Exit to finish process.")
#while True:
#    action = input("Action: ")
#    a = input("First variable: ")
#    b = input("Second variable: ")
#    if a == "Exit" or b == "Exit" or action == "Exit":
#        break
#    else:
#        a = int(a)
#        b = int(b)
#    if action == "Add":
#        print(addition(a, b))
#    elif action == "Sub":
#        print(subtraction(a, b))
#    elif action == "Mult":
#        print(multiplication(a, b))
#    elif action == "Div":
#        print(division(a, b))
#    elif action == "Clear":
#        print(clear)
#    else:
#        pass