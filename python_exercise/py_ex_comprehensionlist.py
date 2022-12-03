Topic = '''List Comprehension
List comprehensions provide a concise way to create lists. 
Common applications are to make new lists where each element is the result of some operations 
applied to each member of another sequence or iterable, or to create a subsequence of those elements 
that satisfy a certain condition.

For example, assume we want to create a list of squares, like
'''
squares = []  # initial list of square is empty
for x in range(10):
    squares.append(x**2)
    print(squares)
print()
sum = []
for x in range(10):
    sum.append(x+2)  # List definition
    print(sum)

print()
Mul_two = []
for x in range(10):
    Mul_two.append(x * 2)  # List definition
    print(Mul_two)
