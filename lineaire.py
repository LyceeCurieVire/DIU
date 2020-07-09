class Pile:
    def __init__(self):
        self.p=[]

    def vide(self):
        return len(self.p)==0

    def push(self,e):
        self.p.append(e)

    def pop(self):
        if self.vide():
            raise Exception
        else:
            return self.p.pop()

    def head(self):
        if self.vide():
            raise Exception
        else:
            return self.p[-1]

class File:
    def __init__(self):
        self.instack=Pile()
        self.outstack=Pile()

    def enfile(self,e):
        self.instack.push(e)

    def defile(self):
        if self.outstack.vide():
            while not self.instack.vide():
                self.outstack.push(self.instack.pop())
        return self.outstack.pop()

    def vide(self):
        return self.instack.vide() and self.outstack.vide()



if __name__=='__main__':
    fifo=File()
    for k in range(5):
        fifo.enfile(k)
    while not fifo.vide():
        print(fifo.defile())

    lifo=Pile()
    for c in 'abcdef':
        lifo.push(c)
    while not lifo.vide():
        print(lifo.pop())
    
