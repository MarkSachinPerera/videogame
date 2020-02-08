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

    # U - user position
    # 0 - Wall, can't move here
    # 1 - Walk area
    # X - marker piece
    # T - Target piece, cover it up.
    # @TODO G - gate piece, next level
    # @TODO W - Successfully covered Target

    my_board = [['0', '0', '0', '0', '0', '0', '0'],
                ['0', '1', '1', '1', '1', '1', '0'],
                ['0', 'T', 'X', '1', '1', '1', '0'],
                ['1', '1', '1', 'U', '1', '1', '0'],
                ['0', '1', '1', '1', 'X', '1', '0'],
                ['0', '1', '1', '1', 'T', '1', '0'],
                ['0', '1', '1', '1', '1', '1', '0'],
                ['0', '0', '0', '0', '0', '0', '0']]

    def __init__(self, parent, square_size=92):
        self.width = 7
        self.height = 8
        self.userX = 3
        self.userY = 3
        canvas_width = self.width * square_size
        canvas_height = self.height * square_size

        self.parent = parent
        self.gif_dirt = PhotoImage(file='dirtblock.png')
        self.gif_tnt = PhotoImage(file='TNT.png')
        self.gif_user = PhotoImage(file='user.png')
        self.gif_blank = PhotoImage(file='blank.png')

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

    def drawBoard(self, square_size=92):
        for row in range(self.height):
            for col in range(self.width):
                x1 = col * square_size
                y1 = (self.height - 1 - row) * square_size
                x2 = x1 + square_size
                y2 = y1 + square_size

                if self.my_board[row][col] == '0':
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="dark gray", tags="square")
                elif self.my_board[row][col] == '1':
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="#02B56B", tags="square")
                    self.canvas.create_image(x1 + (square_size / 2), y1 + (square_size / 2), image=self.gif_blank)
                elif self.my_board[row][col] == 'U':
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="#02B56B", tags="square")
                    self.canvas.create_image(x1 + (square_size / 2), y1 + (square_size / 2), image=self.gif_user)
                elif self.my_board[row][col] == 'T':
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="#02B56B", tags="square")
                    self.canvas.create_image(x1 + (square_size / 2), y1 + (square_size / 2), image=self.gif_tnt)
                elif self.my_board[row][col] == 'X':
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="#02B56B", tags="square")
                    self.canvas.create_image(x1 + (square_size / 2), y1 + (square_size / 2), image=self.gif_dirt)
                elif self.my_board[row][col] == 'W':
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="yellow", tags="square")
                    self.canvas.create_image(x1 + (square_size / 2), y1 + (square_size / 2), image=self.gif_dirt)
        self.canvas.tag_lower("square")

    def leftkey(self, event):
        if self.userX - 1 >= 0:
            self.move(self.userX - 1, self.userY, "Left")
            self.drawBoard()

    def rightkey(self, event):
        if self.userX + 1 < self.width:
            self.move(self.userX + 1, self.userY, "Right")
            self.drawBoard()

    def upkey(self, event):
        if self.userY + 1 < self.height:
            self.move(self.userX, self.userY + 1, "Up")
            self.drawBoard()

    def downkey(self, event):
        if self.userY - 1 >= 0:
            self.move(self.userX, self.userY - 1, "Down")
            self.drawBoard()

    def move(self, new_x, new_y, direction):
        if self.my_board[new_y][new_x] == 'X':

            # couple of cases:
            # 1. Successfully covered target
            # 2. Blocked Direction
            # 3. Other direction

            if direction == "Right":
                if new_x + 1 < self.width:
                    if self.my_board[new_y][new_x + 1] == 'T':
                        self.double_move(new_x, new_y, 'W', 1, 0)
                    elif self.my_board[new_y][new_x + 1] == '1':
                        self.double_move(new_x, new_y, 'X', 1, 0)

            elif direction == "Down":
                if new_y - 1 >= 0:
                    if self.my_board[new_y - 1][new_x] == 'T':
                        self.double_move(new_x, new_y, 'W', 0,  -1)
                    elif self.my_board[new_y - 1][new_x] == '1':
                        self.double_move(new_x, new_y, 'X', 0, -1)

            elif direction == "Up":
                if new_y + 1 < self.height:
                    if self.my_board[new_y + 1][new_x] == 'T':
                        self.double_move(new_x, new_y, 'W', 0,  1)
                    elif self.my_board[new_y + 1][new_x] == '1':
                        self.double_move(new_x, new_y, 'X', 0, 1)

            elif direction == "Left":
                if new_x - 1 >= 0:
                    if self.my_board[new_y][new_x - 1] == 'T':
                        self.double_move(new_x, new_y, 'W', -1, 0)
                    elif self.my_board[new_y][new_x - 1] == '1':
                        self.double_move(new_x, new_y, 'X', -1, 0)

        elif self.my_board[new_y][new_x] == '1':
            self.my_board[new_y][new_x] = 'U'
            self.my_board[self.userY][self.userX] = '1'
            self.userX = new_x
            self.userY = new_y

    def double_move(self, new_x, new_y, board_piece, direction_x, direction_y):
        marker_x = new_x
        marker_y = new_y
        self.my_board[marker_y + direction_y][marker_x + direction_x] = board_piece
        self.my_board[new_y][new_x] = 'U'
        self.my_board[self.userY][self.userX] = '1'
        self.userX = new_x
        self.userY = new_y


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
