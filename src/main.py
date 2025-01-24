from cli import start_repl
from commands import set_wall_to_apod

import datetime
import sys


def __parse_args(args):
    if len(args) > 1:
        for arg in args:
            if arg == "--days":
                try:
                    days = int(args[args.index(arg) + 1])
                    today = datetime.datetime.now()
                    start_date = today - datetime.timedelta(days=days)

                    set_wall_to_apod(start_date)
                except ValueError:
                    print("Invalid argument for --days")
                    sys.exit(1)
                except IndexError:
                    print("No argument found for --days")
                    sys.exit(1)
            if arg == "--help":
                __print_help()

        return True
    return False


def __print_help():
    print("Usage: python3 main.py [options]")
    print("Options:")
    print("\t--days <number>\tSet the wallpaper to the APOD from <number> days ago")
    print("\t--help\t\tPrint this help message")


def main():
    # check command line arguments
    if not __parse_args(sys.argv):
        # if no arguments found start the REPL
        start_repl()


if __name__ == '__main__':
    main()
