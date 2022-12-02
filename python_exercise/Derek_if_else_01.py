# if the age is 5 go to Kindergarten
# age 6 through 17 goes to grade 1 through 12
# if age is greater than 17 say go to college
# try to complete with 10 or less line

# -----Solution -----

# Ask for age
age = eval(input("Enter age: "))
# if age is less than 5, too young for school
if age < 5:
    print("Too young for School")
# if age is 5, go to kindergarten
elif age == 5:
    print("Go to kindergarten")
# if age is between 5 and 17 go to grade 1 through to 12
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("go to {} grade".format(grade))
# else go to college
else:
    print("Go to College")

