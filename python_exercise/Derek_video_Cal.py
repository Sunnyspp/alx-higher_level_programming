# Enter Calculation: 5 * 6
# 5 * 6 = 30

# store the input of 2 numbers and the operators
num1, operator, num2 = input('Enter Calculation: ').split()

# convert the string to integer
num1 = int(num1)
num2 = int(num2)
# if operator is any of +, -, *, and / provide output accordingly
# print the result

if operator == "+":
    print("{} + {} = {}".format(num1, num2, (num1 + num2)))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, (num1 - num2)))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, (num1 * num2)))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, (num1 / num2)))
else:
    print('Use either +, -, * or / next time')
