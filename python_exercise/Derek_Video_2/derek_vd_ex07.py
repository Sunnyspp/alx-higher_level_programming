'''Guessing game using while True and break statement'''
secret_number = 7
while True:
    guess = int(input("Guess a number between 1 and 10 : "))

    if guess == secret_number:
        print("hurray!!! you guessed right")
        break
