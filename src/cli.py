# Command Line Interface for the application

import datetime
from commands import set_wall_to_apod

WELCOME = """Welcome to Abhailels Wall
    A NASA Astronomy Picture of the Day (APOD) downloader and wallpaper engine
"""


def start_repl():

    today = datetime.datetime.now().strftime("%Y-%m-%d")

    print(WELCOME)
    print("Type 'help' for a list of commands")

    print(f"Today's date is {today}")

    while True:
        command = input(">>> ")

        if command == 'exit':
            break
        elif command == 'help':
            print("Commands:")
            print("exit - Exit the program")
            print("set_wall - Set the wallpaper to the Astronomy Picture of the Day")
        elif command.startswith('set_wall'):
            get_date = command.split(' ')
            set_wall_to_apod(today)
        else:
            print("Command not found")
