from time import sleep
from pyfiglet import Figlet
from colorama import Fore

from typingMode import typingMode


def welcome():
    """This function prints the welcome message to the user"""
    title_font = Figlet(font="doom")
    subtitle_font = Figlet(font="digital")
    first_line = "Welcome to\n"
    game_title = title_font.renderText("hangman game")
    typingMode(Fore.LIGHTBLUE_EX + first_line + Fore.RESET)
    print()
    print(Fore.LIGHTRED_EX + game_title + Fore.RESET)
    sleep(0.5)
    print()

    while True:
        user_name = input("Please enter your name: \n")
        if str.isalpha(user_name):
            welcome_message = subtitle_font.renderText(f"Welcome \
to the hangman game, {user_name}")
            print(Fore.LIGHTBLUE_EX + welcome_message + Fore.RESET)
            break
        elif len(user_name) == 0:
            ins_char = "Insufficient characters."
            print(Fore.LIGHTRED_EX + ins_char + Fore.RESET)
            print("Please enter your name or nickname.\n")
        else:
            print("Only letters are allowed")
