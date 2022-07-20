from time import sleep
from pyfiglet import Figlet
from colorama import Fore

from typingMode import typingMode


def welcome():
    """This function prints the welcome message to the user"""
    titleFont = Figlet(font="doom")
    subtitleFont = Figlet(font="digital")
    firstLine = "Welcome to\n"
    gameTitle = titleFont.renderText("hangman game")
    typingMode(Fore.LIGHTBLUE_EX + firstLine + Fore.RESET)
    print()
    print(Fore.LIGHTRED_EX + gameTitle + Fore.RESET)
    sleep(0.5)
    print()

    while True:
        user_name = input("Please enter your name: \n")
        if str.isalpha(user_name):
            welcomeMessage = subtitleFont.renderText(f"Welcome \
            to the hangman game, {user_name}")
            print(Fore.LIGHTBLUE_EX + welcomeMessage + Fore.RESET)
            break
        elif len(user_name) == 0:
            print("Insufficient characters.\
             Please enter your name or nickname.")
        else:
            print("Only letters are allowed")
