print('Welcome to car game Simulation!')
print('Type "help" for options.')

def menu_options():
    print("Type 'help' for options.")
    print("Type 'start' to start the car.")
    print("Type 'stop' to stop the car.")
    print("Type 'quit' to exit the game.")

def simulation():
    car_started = False
    while True:
        user_input = input("> ").lower()
        if user_input == "help":
            menu_options()
        elif user_input == "start":
            if car_started:
                print("Car is already started!")
            else:
                car_started = True
                print("Car started...Ready to go!")
        elif user_input == "stop":
            if not car_started:
                print("Car is already stopped!")
            else:
                car_started = False
                print("Car stopped.")
        elif user_input == "quit":
            break
        else:
            print("Invalid input. Please try again.")

simulation()