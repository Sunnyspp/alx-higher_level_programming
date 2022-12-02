Topic = '''Derek Video work through 2'''
print(Topic)

# to loop through a list:
for i in [2, 4, 5, 7, 8, 9 ]:
    print("i = ", i)
# to loop through a range of 10:
for i in range(10):
    print("\ni = ", i)
# to chack if number is even or odd
# Ask for a number
num = input("Enter a number: ")
# convert the number to int
num = int(num)
# check if the number divided by 2 has a remainder 0
if num % 2 == 0:
    print("The number {} is Even\n".format(num))
else:
    print("The number is odd\n")
