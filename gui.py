from tkinter import *
from PIL import ImageTk


class Window:
    def __init__(self,game):
        ##create a window and a canvas
        self.game = game
        self.window = Tk()
        self.window.title('tic tac toe')
        self.window.iconbitmap(r"media\icon.ico")
        self.canvas = Canvas(self.window, width = 852, height = 480, bg = 'brown')
        self.canvas.bind('<Button-1>', self.getxy)
        self.canvas.grid()
        ##draw the background
        self.background = ImageTk.PhotoImage(file = r"media\background.jpg")
        self.background_seen = self.canvas.create_image(0,0,image = self.background ,anchor = NW)
        ##add images for x and o
        self.x_im = ImageTk.PhotoImage(file = r"media\x.png")
        self.o_im = ImageTk.PhotoImage(file = r"media\o.jpg")

    def getxy(self,event):
        if self.game.turn = 'X':
            self.canvas.create_image(event.x, event.y, image = self.x_im )
        if self.game.turn = 'O':
            self.canvas.create_image(event.x, event.y, image = self.o_im )
        self.window.update()
        print("Position = ({0},{1})".format(event.x, event.y))
