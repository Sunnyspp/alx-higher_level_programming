"""Program to calculate the interest of a

ten years investment"""

# Ask the user to enter the Amount to invest

amount = input("Enter the amount to invest: ")

# Ask the user to enter the interest rate

interest_rate = input("Enter the interest rate: ")

# Convert the string of Amount and interest rate to float

amount = float(amount)

interest_rate = float(interest_rate) * .01

# circle through ten years

for i in range(10):

    amount = amount + (amount * interest_rate)

# out put the result

print("Amount in ten years of investment is: {:.2f}".format(amount))
