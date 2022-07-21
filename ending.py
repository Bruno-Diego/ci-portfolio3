from time import sleep
from pyfiglet import Figlet
from colorama import Fore

from typingMode import typingMode


def game_over():
    """
    GAME OVER ascii art with figlet
    """
    gameOverTitleFont = Figlet(font="larry3d")
    gameOverText = gameOverTitleFont.renderText("Game Over")
    print(Fore.LIGHTRED_EX + gameOverText + Fore.RESET)
    typingMode("Better luck next time!\n")
    print()


def you_win():
    """
    Success ascii art with figlet
    """
    print()
    youWinTitleFont = Figlet(font="larry3d")
    youWinText = youWinTitleFont.renderText("You Win")
    print(Fore.LIGHTBLUE_EX + youWinText + Fore.RESET)
