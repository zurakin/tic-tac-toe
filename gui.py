from tkinter import *
from PIL import ImageTk


class Window:
    def __init__(self,game):
        ##create a window and a canvas
        self.game = game
        self.window = Tk()
        self.window.title('tic tac toe')
        self.window.iconbitmap(r"media\icon.ico")
        self.canvas = Canvas(self.window, width = 600, height = 600, bg = 'brown')
        self.canvas.bind('<Button-1>', self.getxy)
        self.canvas.grid()
        ##draw the background
        self.background = ImageTk.PhotoImage(file = r"media\background.png")
        self.background_seen = self.canvas.create_image(0,0,image = self.background ,anchor = NW)
        ##add images for x and o
        self.x_im = ImageTk.PhotoImage(file = r"media\x.png")
        self.o_im = ImageTk.PhotoImage(file = r"media\o.png")

    def getxy(self,event):
        if self.game.turn == 'X':
            self.canvas.create_image(int(event.x/200)*200, int(event.y/200)*200, image = self.x_im ,anchor = NW)
            self.game.turn = 'O'
        elif self.game.turn == 'O':
            self.canvas.create_image(int(event.x/200)*200, int(event.y/200)*200, image = self.o_im,anchor = NW )
            self.game.turn = 'X'
        self.window.update()
        print("Position = ({0},{1})".format(int(event.x/200), int(event.y/200)))
