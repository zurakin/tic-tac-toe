import gui
import game

def execute(*args):
    global games_count
    games_count += 1
    for im in root.images:
        root.canvas.delete(im)
        root.window.update()


games_count = 0
current_game = game.Game(games_count)
root = gui.Window(current_game)
root.window.bind('<Return>',execute)
root.window.update()
root.window.mainloop()
