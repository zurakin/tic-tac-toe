from tkinter import *
from PIL import ImageTk


def convert(pos):
    return pos[1]*3 + pos[0]


class Window:
    def __init__(self,game):
        ##create a window and a canvas
        self.game = game
        self.window = Tk()
        self.window.title('tic tac toe')
        self.window.iconbitmap(r"media\icon.ico")
        self.canvas = Canvas(self.window, width = 600, height = 600,
         bg = 'brown')
        self.canvas.bind('<Button-1>', self.click)
        self.canvas.grid()
        ##draw the background
        self.background = ImageTk.PhotoImage(file = r"media\background.png")
        self.background_seen = self.canvas.create_image(0,0,
        image = self.background ,anchor = NW)
        ##add images for x and o
        self.x_im = ImageTk.PhotoImage(file = r"media\x.png")
        self.o_im = ImageTk.PhotoImage(file = r"media\o.png")
        self.hbar = ImageTk.PhotoImage(file = r"media\hbar.png")
        self.vbar = ImageTk.PhotoImage(file = r"media\vbar.png")
        self.diaglr = ImageTk.PhotoImage(file = r"media\diaglr.png")
        self.diagrl = ImageTk.PhotoImage(file = r"media\diagrl.png")
        self.images = []
        self.lines = {
        (0,1,2):(self.hbar,(0,0)),
        (3,4,5):(self.hbar,(0,200)),
        (6,7,8):(self.hbar,(0,400)),
        (0,3,6):(self.vbar,(0,0)),
        (1,4,7):(self.vbar,(200,0)),
        (2,5,8):(self.vbar,(400,0)),
        (0,4,8):(self.diaglr,(0,0)),
        (2,4,6):(self.diagrl,(0,0))
        }

    def click(self,event):
        if self.game.winner != None:
            return
        if self.game.table[convert((int(event.x/200), int(event.y/200)))] != None:
            return
        if self.game.turn == 'X':
            self.game.table[convert((int(event.x/200), int(event.y/200)))] = 'X'
            self.images.append(self.canvas.create_image(int(event.x/200)*200,
            int(event.y/200)*200, image = self.x_im ,anchor = NW))
            self.game.turn = 'O'
        elif self.game.turn == 'O':
            self.game.table[convert((int(event.x/200), int(event.y/200)))] = 'O'
            self.images.append(self.canvas.create_image(int(event.x/200)*200,
            int(event.y/200)*200, image = self.o_im,anchor = NW ))
            self.game.turn = 'X'

        self.window.update()
        winning_line = self.game.check_winner()
        if winning_line!= None:
            self.images.append(self.canvas.create_image(self.lines[winning_line][1][0],
            self.lines[winning_line][1][1],
            image = self.lines[winning_line][0],
            anchor = NW))


        if self.game.winner != None:
            print('the winner is {}\nPress return to restart'.format(self.game.winner))
