#!/usr/bin/python3

# from tkinter import *
import random

my_board = [ ('0', '0', '0', '0', '0', '0', '0'),
             ('0', '1', '1', '1', '1', '1', '0'),
             ('0', '1', '1', 'x', '1', '1', '0'),
             ('0', '1', '1', '1', '1', '1', '0'),
             ('0', '0', '0', '0', '0', '0', '0')]

HEIGHT = 5
WIDTH = 7


def printBoard():
    print(" ---" * len(my_board[0]))

    for i in my_board:
        print("|", end=' ')
        for j in i:
            print("%s |" % j, end=' ')
        print("")
        print(" ---" * len(my_board[0]))

def main():
    print("Welcome to my game!\n")
    print("0 - means a wall")
    print("1 - means a path to walk on")
    print("x - is the user")
    print("Use the arrow keys to move around")

    printBoard()



if __name__ == '__main__':
    main()