Topic = """List comprehension cont."""
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

combs = []
for x in [1, 2, 3]:
    for y in [3,1, 4]:
        combs.append((x, y))
print(combs)

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]
print(vec)

# The del statement
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
