# price of house
price = 1000000
# if the buyer has good credit put down 10%
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"Down payment: ${down_payment}")
# ====== using logical operator ======
has_high_income = False
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")
if has_high_income or has_good_credit:
    print("Eligible for half the loan")

# using comparison operator
temperature = 30
if temperature > 30:
    print("it is a hot day")
else:
    print("it is not a hot day")

# ========= Exercise =========
name = "Jaze"
if len(name) < 3:
    print("Name must be at least 3 character")
elif len(name) > 50:
    print("Name must be a maximum of 50 character")
else:
    print("Name looks good!")
# ======= exercize on weight conversion =======
# Enter your weight in pounds and get the result in kg and vice versa
weight = eval(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
# ======= While loops ======
a  = 1
while a <= 5:
    print('*' * a)
    a += 1
print("done")

# ====== Building a guessing game ========
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = eval(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('Hurray!!!You win!')
        break
else:
    print("Sorry you are out of guess!!!")
