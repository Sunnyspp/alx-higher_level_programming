# ====== For loop ======
for item in ['sunny', 'Alexis', 'Sammy']:
    print(item)
    # ===== For loops in range =====
print()
for numbers in range(11):
    print(numbers)
print()
print("To iterate through in to ten")
for numberInTens in range(10, 110, 10):
    print(numberInTens)
# ======= calculate the total price of object =====
print("To calculate the total price of object")
prices = [10, 20, 30, 40]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")
# ===== Nested loop ======
# ======== Generate a list of coordinate ========
print("To generate coordinate")
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')
print("done")
# ======= Using nested loop =====
'''
draw the
xxxxx
xx
xxxxx
xx
xx
'''
print()
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print('x' * x_count)
print()

nums = [5, 2, 5, 2, 2]
for x_count in nums:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
print("done")

nums = [2, 2, 2, 2, 2, 9,]
for l_count in nums:
    output = ''
    for count in range(l_count):
        output += 'l'
    print(output)
print("done")
