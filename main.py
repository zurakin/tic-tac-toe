import gui
import game


games_count = 0

def execute(*args):
    global games_count
    games_count += 1
    current_game = game.Game(games_count)
    root = gui.Window(current_game)
    root.window.bind('<Return>',execute)
    root.window.update()
    root.window.mainloop()


execute()
