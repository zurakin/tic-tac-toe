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
        self.images = []

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
        self.game.check_winner()
        if self.game.winner != None:
            print('the winner is {}\nPress return to restart'.format(self.game.winner))
