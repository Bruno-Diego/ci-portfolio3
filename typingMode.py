import sys
from time import sleep


def typingMode(text):
    '''typingMode will print the text letter by letter on terminal'''
    for char in text:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
