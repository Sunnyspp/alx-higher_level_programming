'''
How to handle errors using while loop with True
'''
while True:
    try:
        number = int(input("Please enter a number : "))
        break
    except ValueError:
        print("you didn't enter a number")

    except:
        print("An unknown error occurred")
print("Thank you for entering a number")
