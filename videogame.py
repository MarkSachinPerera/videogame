#!/usr/bin/python3

from tkinter import *
import _curses as curses

# def printBoard():
#     print(" ---" * len(my_board[0]))
#
#     for i in my_board:
#         print("|", end=' ')
#         for j in i:
#             print("%s |" % j, end=' ')
#         print("")
#         print(" ---" * len(my_board[0]))


class boardGame(Frame):

    # @property
    # def canvas_size(self):
    #     return(self.width * square_size, self.height * square_size)

    my_board = [['0', '0', '0', '0', '0', '0', '0'],
                ['0', '1', '1', '1', '1', '1', '0'],
                ['0', '1', '1', '1', '1', '1', '0'],
                ['0', '1', '1', 'x', '1', '1', '0'],
                ['0', '1', '1', '1', '1', '1', '0'],
                ['0', '1', '1', '1', '1', '1', '0'],
                ['0', '1', '1', '1', '1', '1', '0'],
                ['0', '0', '0', '0', '0', '0', '0']]

    def __init__(self, parent, square_size=30):
        self.width = 7
        self.height = 8
        self.userX = 3
        self.userY = 3
        canvas_width = self.width * square_size
        canvas_height = self.height * square_size

        self.parent = parent
        # self.S = PhotoImage(file='sample-gif-2.gif')

        Frame.__init__(self, parent)

        self.canvas = Canvas(self, width=canvas_width, height=canvas_height, bg="white")
        # self.canvas.create_image(480, 480, image=self.gif1, anchor=NW)
        self.canvas.bind("<Left>", self.leftkey)
        self.canvas.bind("<Right>", self.rightkey)
        self.canvas.bind("<Up>", self.upkey)
        self.canvas.bind("<Down>", self.downkey)
        print("Use the arrow keys to move around")
        # self.canvas.bind("<Button-1>", self.click)

        self.canvas.pack(side="top", fill="both", anchor="c", expand=True)

        self.canvas.focus_set()  # This will send pressed keys

        '''
        fill − Determines whether widget fills any extra space allocated to it by the packer, 
        or keeps its own minimal dimensions: NONE (default), X (fill only horizontally), 
        Y (fill only vertically), or BOTH (fill both horizontally and vertically).
        '''

    def drawBoard(self, square_size=30):
        for row in range(self.height):
            for col in range(self.width):
                x1 = col * square_size
                y1 = (self.height - 1 - row) * square_size
                x2 = x1 + square_size
                y2 = y1 + square_size

                if self.my_board[row][col] == '0':
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="dark gray", tags="square")
                elif self.my_board[row][col] == '1':
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="green", tags="square")
                elif self.my_board[row][col] == 'x':
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="red", tags="square")
        self.canvas.tag_lower("square")

    def leftkey(self, event):
        newX = self.userX - 1
        newY = self.userY

        self.my_board[newY][newX] = 'x'
        self.my_board[self.userY][self.userX] = '1'

        # self.userX

        self.drawBoard()


    def rightkey(self, event):
        print("pressed : left")

    def upkey(self, event):
        print("pressed : left")

    def downkey(self, event):
        print("pressed : left")

    # def click(self, event):
    #     print("clicked")


def main():
    print("Welcome to my game!\n")
    # print("0 - means a wall")
    # print("1 - means a path to walk on")
    # print("x - is the user")
    # print("Use the arrow keys to move around")

    mywindow = Tk()  # main window that i will be editing

    board = boardGame(mywindow)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    board.drawBoard()

    mywindow.mainloop()


if __name__ == '__main__':
    main()
