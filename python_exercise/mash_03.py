# ======= Car Game ======
command = ""
started = False
while True:
    command = input("> "). lower()
    if command == "start":
        if started:
            print("Car is already started!!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!!")
        else:
            started = False
        print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit the process
""")
    elif command == "quit":
        print("Are you sure you want to quit!")
        response = input("Enter (Yes) or (No): ")
        if response == "No":
            print("please continue")
            continue
        elif response == "Yes":
            print("Game over!")
            break
    else:
        print("Please i don't understand")
