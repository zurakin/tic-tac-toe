from position import *
from player import *

strikes=["012","345","678","036","147","258","048","246"]
class Game:
    def __init__(self,number):
        self.turn = 'X'
        self.number=number
        self.winner=None
        self.sheet={i:Pos(i) for i in range(9)}

    def draw(self):
        for i in range(3):
            print("{}\t{}\t{}\n".format(str(3*i)+' : '+self.sheet[3*i].__repr__(),str(3*i+1)+' : '+self.sheet[3*i+1].__repr__(),str(3*i+2)+' : '+self.sheet[3*i+2].__repr__()))

    def list_pw(self):
        global strikes
        return [ [ self.sheet[int(pos)] for pos in L ] for L in strikes]

    def check_winner(self):
        for p in self.list_pw():
            if all([ i.content == 'X' for i in p]):
                self.winner='X'
                return 'X'
        for p in self.list_pw():
            if all([ i.content == 'O' for i in p]):
                self.winner='O'
                return "O"
        if self.winner==None and all([self.sheet[i].__repr__()!='_' for i in range(9)]):
            self.winner=='draw'
        return None


    #player is the one who starts first , is equ to 'X' or 'O'
    def play(self,player):
        ord=[player]
        if player=="X":
            ord.append("O")
        else:
            ord.append("X")

        p1=Player(ord[0],self)
        p2=Player(ord[1],self)

        while True:
            self.draw()
            print(ord[0]+"'s turn :")

            while True:
                try:
                    p1.play(int(input()))
                    break
                except:
                    print('position already contains a piece')
            if self.check_winner() != None:
                return self.check_winner()
            self.draw()
            print(ord[1]+"'s turn :")

            while True:
                try:
                    p2.play(int(input()))
                    break
                except:
                    print('position already contains a piece')
            if self.check_winner() != None:
                return self.check_winner()
