
List=["012","345","678","036","147","258","048","246"]


[i  for L in [[1,2,3]] for i in L]


class Game:
    def __init__(self,number):
        self.number=number
        self.winner=None
        self.sheet={i:Pos(i) for i in range(9)}

    def draw(self):
        for i in range(3):
            print("{}\t{}\t{}\n".format(str(3*i)+' : '+self.sheet[3*i].__repr__(),str(3*i+1)+' : '+self.sheet[3*i+1].__repr__(),str(3*i+2)+' : '+self.sheet[3*i+2].__repr__()))

    def list_pw(self):
        global List
        return [ [ self.sheet[int(pos)] for pos in L ] for L in List]

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

        p1=Player(ord[0])
        p2=Player(ord[1])

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


class Player:
    def __init__(self,nature):
        self.nature=nature

    def play(self,pos):
        global current_game
        assert current_game.sheet[pos].content == None
        current_game.sheet[pos].content=self.nature


class Pos:
    def __init__(self,number):
        self.content=None
        self.number=number

    def __repr__(self):
        if self.content==None:
            return "_"
        else :
            return self.content


if __name__=="__main__":
    ord=['X','O']
    i=0
    while True:
        current_game=Game(i)
        w=current_game.play(ord[i%2])
        if w!='draw':
            print(w+ ' wins !')
        else:
            print("it's a draw")
        if input("type 'END' to end the game, to continue just hit enter")=='END':
            break
        i+=1
