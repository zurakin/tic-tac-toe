
strikes=["012","345","678","036","147","258","048","246"]
class Game:
    def __init__(self,number):
        self.turn = 'X'
        self.number=number
        self.winner=None
        self.table={i:None for i in range(9)}

    def list_pw(self):
        global strikes
        return [ [ int(pos) for pos in L ] for L in strikes]

    def check_winner(self):
        for p in self.list_pw():
            if all([ self.table[i] == 'X' for i in p]):
                self.winner='X'
                return tuple(p)
        for p in self.list_pw():
            if all([ self.table[i] == 'O' for i in p]):
                self.winner='O'
                return tuple(p)
        if self.winner==None and all([self.table[i]!=None for i in range(9)]):
            self.winner=='draw'
        return
