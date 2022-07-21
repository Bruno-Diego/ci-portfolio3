import random
import time
from welcome import welcome
from ending import game_over, you_win
from word import getWord
from pyfiglet import Figlet
from colorama import Fore
from typingMode import typingMode


# Setting the stage number to be used as limit for incorrect attempts
STAGES = ['\n  +---+\n  |   |\n      |\n\
      |\n      |\n      |\n=========\n',
          '\n  +---+\n  |   |\n  O   |\n\
      |\n      |\n      |\n=========\n',
          '\n  +---+\n  |   |\n  O   |\n\
  |   |\n      |\n      |\n=========\n',
          '\n  +---+\n  |   |\n  O   |\n\
 /|   |\n      |\n      |\n=========\n',
          '\n  +---+\n  |   |\n  O   |\n\
 /|\  |\n      |\n      |\n=========\n',
          '\n  +---+\n  |   |\n  O   |\n\
 /|\  |\n /    |\n      |\n=========\n',
          '\n  +---+\n  |   |\n  O   |\n\
 /|\  |\n / \  |\n      |\n=========\n| LAST CHANCE!\n']

ATTEMPTS = len(STAGES)


def display_instructions():
    """
    Ask user if instruction is need and displays instruction as requested
    """
    instruction_q = "Would you like a brief instruction on how to play?"
    print(Fore.LIGHTBLUE_EX + instruction_q + Fore.RESET)
    instruction_on = input("Press y if yes, any other key to play game : \n")
    if instruction_on.lower() == "y":
        instructions_text()
        ready_q = "Are you ready to play?"
        print(Fore.LIGHTBLUE_EX + ready_q + Fore.RESET)
        input("Press Any key to start the game >> \n")
    else:
        pass


def instructions_text():
    """
    Display instructions
    """
    present_instr = "Here are the instructions on how to play:\n"
    print()
    print(Fore.LIGHTBLUE_EX + present_instr + Fore.RESET)
    print("1. A random word is chosen by the computer\n"
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
    print()


def start_game():
    """
    Main game function to display questions, check the answer and
    count attempts.
    Repeats process if game completion condition is not met.
    Either word completion or reaching full stages will end the game.
    """
    incorrect = 0    # Setting the starting point of incorrect attempts
    correct_guess = set([])   # Creating a empty list to store correct answers
    word = getWord().upper()    # Random word chosen by the function
    answers = [i for i in word]    # Create list from the word
    wrong_guess = []   # Incorrect letters goes in here
    while incorrect < ATTEMPTS:
        display_guess_message()
        # Print out _ for the remaining letters to guess
        for i in word:
            if i in correct_guess:
                print(Fore.LIGHTBLUE_EX + i + Fore.RESET, end=" ")
            else:
                empty_space = "_"
                print(Fore.LIGHTRED_EX + empty_space + Fore.RESET, end=" ")
        print('\n')
        guessed = input("Enter one letter please!\n").upper()
        if str.isalpha(guessed):  # Checking if the input is non-numeric
            if len(guessed) > 1:
                print("***** Please input one letter at a time *****")
                time.sleep(1)
            elif guessed in answers:
                # Checking the answer and determine action
                if guessed in correct_guess:
                    display_already_used()
                    time.sleep(1)
                else:
                    right_letter = f"{guessed.upper()} is the right answer!"
                    print(Fore.LIGHTBLUE_EX + right_letter + Fore.RESET)
                    correct_guess.add(guessed)  # Add correct letter to list
                    if correct_guess == set(word):
                        typingMode(word.upper())
                        print()
                        print("CONGRATULATIONS!")
                        print(f"You completed the word {word.upper()}.")
                        you_win()
                        break
                    time.sleep(1)
            elif guessed in wrong_guess:
                display_already_used()
                time.sleep(1)
            else:
                wrong_letter = f"'{guessed.upper()}' is not in correct answer!"
                print(Fore.LIGHTRED_EX + wrong_letter + Fore.RESET)
                incorrect += 1    # Increment incorrect attempt
                if incorrect == ATTEMPTS:
                    reveal_word = f"Answer is {word.upper()}"
                    typingMode(Fore.LIGHTRED_EX + reveal_word + Fore.RESET)
                    game_over()
                    break
                else:
                    print(STAGES[incorrect])  # Display hangman image
                    wrong_guess.append(guessed.upper())
                    print(f"Your incorrect guesses: {wrong_guess} ")
                    time.sleep(1)
        elif len(guessed) == 0:
            print("Insufficient characters. Please input a letter.\n")
        else:
            print("Only letters are allowed")
    time.sleep(1)
    replay()


def display_guess_message():
    print("\n")
    print("Can you guess the word?")
    print("Enter one letter to see if you are right!")


def display_already_used():
    print("You already tried this one, try again!")


def replay():
    typingMode("Would you like to play again?")
    print()
    retry_game = "Enter y or press RUN PROGRAM button above to play again."
    print(Fore.LIGHTBLUE_EX + retry_game + Fore.RESET)
    print("or press any other key to exit the game.")
    play_again = input(
        "Please press y to play, any other key to exit the game \n")
    if play_again.lower() == "y":
        start_game()
    else:
        print("Thank you for playing the game")
        time.sleep(1)


def main():
    welcome()  # greeting function
    display_instructions()  # display instruction if user chooses
    start_game()


main()
