Topic = '''Data Structure'''
print(Topic) # prints the topic
foods = ['rice', 'beans', 'plantain', 'Semo']
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits) # prints the list of fruits
fruits_it = iter(fruits) # Return an iterator from a tuple, and print each value as below:
print(next(fruits_it))
print(next(fruits_it))
print(next(fruits_it))
print(next(fruits_it))
print(next(fruits_it))
print(next(fruits_it))
print(next(fruits_it))
print(foods) # prints the list of foods
fruits.append(foods) # Appends foods to the list of fruits
print(fruits)  # prints the list of fruits with the appended food in one list.
fruits.append('grape') # Appends grape to the list of fruits
print(fruits)  # prints the list of fruits with grape inclusive in the list
fruits.reverse()  # Reverse the elements of the list in place.
print(fruits)  # prints the fruits from the reverse
print(fruits.count('apple'))  # counts the number of apple in the list of fruits and prints the number
print(fruits)
print(fruits.pop(6)) # removes the item in the position from the list and prints it
print(fruits.count('tangerine'))  # Return the number of times x appears in the list.
print(fruits.count('apple'))  # Return the number of times x appears in the list.
print(fruits.index('banana', 4))  # Find next banana starting from position 4 in the list fruits
print(fruits)
fruits.clear()  # clears the list
print(fruits)  # prints at empty list
del fruits[:]  # Alternative method to clear the list
print(fruits)  # prints at empty list
# list.append(x)
a = ["apple", "banana", "cherry"]
print(a)
a.copy() # Return a shallow copy of the list. Equivalent to a[:].
print(a)
a.pop(0)
print(a)
b = ["Ford", "BMW", "Volvo", "FORD"]
print(b)
b.sort() # Sort the items of the list in place
print(b)
b.copy()  # Return a shallow copy of the list. Equivalent to a[:].
print(b)
b.pop(2) # Remove the item at the given position in the list,
print(b)
b.sort()
print(b)
a.append(b)
print(a)
a.copy()
print(a)
# list.extend(iterable)
favFruits = ("apple", "banana", "cherry")
fav_it = iter(favFruits) # Return an iterator from a tuple, and print each value:
print(next(fav_it))
print(next(fav_it))
print(next(fav_it))
