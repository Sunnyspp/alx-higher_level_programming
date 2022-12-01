# Ask the user to input 2 values and store them in variable num1 num2
num1, num2 = input("Enter two numbers: ").split()

# convert the strings into regular numbers integer
num1 = int(num1)
num2 = int(num2)
# Add the values entered and store in sum
sum = num1 + num2

# subtract values and store in difference
difference = num1 - num2

# Multiply the values and store in product
product = num1 * num2

# Divide the value and store in Quotient
Quotient = num1 / num2

# Use modulus on the values to find the Reminder

Remainder = num1 % num2

# print the result
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, Quotient))
print("{} % {} = {}".format(num1, num2, Remainder))
