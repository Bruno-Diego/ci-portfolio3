import random
import time
from welcome import welcome


# Setting the stage number to be used as limit for incorrect attempts
stages = ['\n  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========\n',
          '\n  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========\n',
          '\n  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========\n',
          '\n  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========\n',
          '\n  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========\n',
          '\n  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========\n',
          '\n  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n',
          '\n  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n| LAST CHANCE!\n']
attempts = len(stages)



def display_instructions():
    """
    Ask user if instruction is need and displays instruction as requested
    """
    print("Would you like a brief instruction on how to play?")
    instruction_on = input("Press y if yes, any other key to play game : \n")
    if instruction_on.lower() == "y":
        instructions_text()
        print("Are you ready to play?")
        game_start = input("Press Any key to start a game >> \n")
    else:
        pass


def instructions_text():
    """
    Display instructions
    """
    print("Here is instruction on how to play \n"
          "1. A random word is chosen by the computer\n"
          "2. The same number of Underscores '_' will be displayed \n"
          "   as letters in the word.\n"
          "3. Guess the word\n"
          "   Only one alphabet key should be entered at each time.\n"
          "   There's pace between the words is considered incorrect.\n"
          "4. If your answer is correct, the letter will be displayed\n"
          "   instead of the underscore'_'.\n"
          "5. If you guess all the letters and complete the word,\n"
          "   you win the game\n"
          "7. If the incorrect answer is entered,"
          " the hangman image will progress.\n"
          "8. If the number of incorrect attempts reaches the limit\n"
          "   and hangman image completes, game over!")




def main():
    welcome()  # greeting function
    display_instructions()  # display instruction if user chooses
    start_game()


main()