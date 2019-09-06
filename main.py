from position import *
from game import *
import gui

current_game = Game(1)
root = gui.Window(current_game)
root.window.update()
root.window.mainloop()
