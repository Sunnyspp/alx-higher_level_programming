name = input('what is your name? ')
print('Hi ' + name)

name = input("What is your name? ")
color = input("What is your favorite colour? ")
print("{} likes {}".format(name, color))
print(name + ' likes ' + color)  # concatenating method
# ===== Types conversion =======
birth_year = input("Birth year: ")
print(type(birth_year))
age = 2022 - int(birth_year)
print(type(age))
print(age)

weight_pounds = input("weight in pounds: ")
weight_pounds = int(weight_pounds)
weight_kg = weight_pounds * 0.45
print("Your weight in kg is ",weight_kg)
