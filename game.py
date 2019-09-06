
strikes=["012","345","678","036","147","258","048","246"]
class Game:
    def __init__(self,number):
        self.turn = 'X'
        self.number=number
        self.winner=None
        self.table={i:None for i in range(9)}

    def list_pw(self):
        global strikes
        return [ [ self.table[int(pos)] for pos in L ] for L in strikes]

    def check_winner(self):
        for p in self.list_pw():
            if all([ i == 'X' for i in p]):
                self.winner='X'
                return 'X'
        for p in self.list_pw():
            if all([ i == 'O' for i in p]):
                self.winner='O'
                return "O"
        if self.winner==None and all([self.table[i]!=None for i in range(9)]):
            self.winner=='draw'
        return None
