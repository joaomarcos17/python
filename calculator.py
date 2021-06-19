# a basic calculator in Python !!
num1 = float(input("Enter a Number:")) # you can use int or float , I used floats bacause it works with floating numbers !!
op = input("Choose an operator:")
num2 = float(input("Enter another Number:"))
# this calculator makes basic operations such as + - * /
if op == "*":
    print(num1 * num2)    # calculate num1 * num2 
elif op == "/":
    print(num1 / num2)   # devide num1 / num2 
elif op == "+":
    print(num1 + num2)     # add num1 + num2 
elif op == "-":
    print(num1 - num2)    # subtract num1 - num2 
else:
    print("Invalid Input!") # in case the input is not a number !!
