Topic = """Lists
Python knows a number of compound data types, used to group together other values. 
The most versatile is the list, which can be written as a list of comma-separated values (items) 
between square brackets. Lists might contain items of different types, 
but usually the items all have the same type.
"""
print(Topic)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)
# now remove them
letters[2:5] = []
print(letters)
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)
# The built-in function len() also applies to lists:
letters = ['a', 'b', 'c', 'd']
print(len(letters))
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])  # indexing returns the item
print(squares[-1])
print(squares[-3:])  # slicing returns a new list
print(squares[:])  # shallow copying
print(squares + [36, 49, 64, 81, 100])  # Concatenating list
cubes = [1, 8, 27, 65, 125]  # something's wrong here
print(4 ** 3)  # the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
print(cubes)
# Append by using append() method
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print(cubes)
# It is possible to nest lists (create lists containing other lists), for example:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
y = [n, a]
print(y)
print(x[0])
print(x[1])
print(y[0])
print(y[1])
print(x[0][1])
#print(y[0][1])
