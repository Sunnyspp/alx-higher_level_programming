# if the age is 5 go to Kindergarten
# age 6 through 17 goes to grade 1 through 12
# if age is greater than 17 say go to college
# try to complete with 10 or less line
# -----Solution -----

# collect age and store result in age.
age = eval(input("Enter age: "))
# if age is 5 or less go to kindergarten
if (age > 0) and (age <= 5):
    print("Go to kindergarten")
# else if age is 6 to 17 go to grade 1 through to 12
elif(age > 6) and (age <= 17):
    if(age > 0) and (age >= 10):
        print("Go and write a test to qualify for a grade between 1 to 6")
    elif(age < 10) and (age <= 17):
        print("Go and write a test to qualify for a grade between 7 to 12")
# else if age is above 17 then go to college
elif(age > 17) and (age < 65):
    print("Go to college")
else:
    print("Sorry, You are above schooling age")

