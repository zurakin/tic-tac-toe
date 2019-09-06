
class Pos:
    def __init__(self,number):
        self.content=None
        self.number=number

    def __repr__(self):
        if self.content==None:
            return "_"
        else :
            return self.content
