import sys

start_game = input("> ")
start = "to start the car"
stop = "to stop the car"
exit = "to quit the game"


def start_stop_exit():
    print(f'''
start - {start}
stop - {stop}
quit {exit}
    ''')


if start_game.lower() != "help":
    while start_game.lower() != "help":
        print("i don't understand")
        start_game = input("> ")
        if start_game.lower() == "help":
            print(start_stop_exit())
else:
    print(start_stop_exit())

controls = ["start", "stop", "exit"]

enter_your_choice = input("> ")


def car_movement():
    starting = "car started..... ready to go"
    stopping = "car stopped"
    quit = "exiting the game"

    if enter_your_choice.lower() == 'start':
        print(starting)
    elif enter_your_choice.lower() == 'stop':
        print(stopping)
    elif enter_your_choice.lower() == 'exit':
        print(quit)
        sys.exit()


print(car_movement())