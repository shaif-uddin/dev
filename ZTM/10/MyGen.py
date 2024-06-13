class MyGen():
    def __init__(self,first,last):
        self.first=first
        self.last=last
    def __iter__(self):
        return self
    def __next__():
        if MyGen.current<self.last:
            num=MyGen.current
            MyGen.currnet+=1
            return num

gen- MyGen(0,10)