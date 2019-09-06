
class Player:
    def __init__(self,nature,game):
        self.nature = nature
        self.game = game

    def play(self,pos):
        assert self.game.sheet[pos].content == None
        self.game.sheet[pos].content=self.nature
