# Receive age and store in age
age = eval(input("Enter age: "))

# and : if both conditions are true it returns True
# or : if either conditions is true it returns True
# not : Convert the true to false vice verser

# if age is both greater than or equal to and less than
if (age >= 1) and (age <= 18):
    print("Important Birthday")
elif (age == 21) or (age == 50):
    print("Important Birthday")
elif not(age < 65):
    print("Important Birthday")
else:
    print("Sorry not Important")

