#!/usr/bin/python3

from tkinter import *

my_board = [('0', '0', '0', '0', '0', '0', '0'),
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


class boardGame(Frame):
    width = 6
    height = 6

    # @property
    # def canvas_size(self):
    #     return(self.width * square_size, self.height * square_size)

    def __init__(self, parent, square_size=30):
        canvas_width = self.width * square_size
        canvas_height = self.height * square_size

        self.parent = parent
        self.gif1 = PhotoImage(file='sample-gif-2.gif')

        Frame.__init__(self, parent)

        self.canvas = Canvas(self, width=canvas_width, height=canvas_height)
        self.canvas.create_image(480, 480, image=self.gif1, anchor=NW)
        self.canvas.bind("<Key>", self.key)
        print("Use the arrow keys to move around")
        self.canvas.bind("<Button-1>", self.click)

        self.canvas.pack(side="top", fill="both", anchor="c", expand=True)
        
        self.canvas.pack()

        self.canvas.focus_set()

        '''
        fill − Determines whether widget fills any extra space allocated to it by the packer, 
        or keeps its own minimal dimensions: NONE (default), X (fill only horizontally), 
        Y (fill only vertically), or BOTH (fill both horizontally and vertically).
        '''

    def key(self, event):
        print("pressed ")
        self.canvas.focus_set()


    def click(self, event):
        print("clicked")



def main():
    print("Welcome to my game!\n")
    # print("0 - means a wall")
    # print("1 - means a path to walk on")
    # print("x - is the user")
    # print("Use the arrow keys to move around")

    mywindow = Tk()  # main window that i will be editing

    board = boardGame(mywindow)
    board.pack(side="top", fill="both", expand="true")

    mywindow.mainloop()


if __name__ == '__main__':
    main()
