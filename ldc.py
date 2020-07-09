class Liste:
    def __init__(self,l=[]):
        self.fst=None
        self.lst=None
        self.t=0
        if l:
            for k in l:
                self.adjq(Cellule(k))

    def adjq(self,e):
        d=self.lst
        if d:
            d.setSuivant(e)
            e.setPrecedent(d)
        else:
            e.setPrecedent(None)
            self.fst=e
        e.setSuivant(None)
        self.lst=e
        self.t+=1

    def dernier(self):
        return self.lst

    def supprDernier(self):
        if self.lst:
            d=self.lst.getPrecedent()
            self.lst=d
            if d:
                d.setSuivant(None)
            else:
                self.fst=None
            self.t-=1
        
    def premier(self):
        return self.fst

    def supprPremier(self):
        if self.fst:
            d=self.fst.getSuivant()
            self.fst=d
            if d:
                d.setPrecedent(None)
            else:
                self.lst=None
        self.t-=1


    def taille(self):
        return self.t

    def get(self,i):
        if 2*i<self.t:
            return self.getfwd(i)
        else:
            return self.getbwd(i)

    def getfwd(self,i):
        k=0
        c=self.fst
        while k<i and c:
            k+=1
            c=c.getSuivant()
        if k==i:
            return c
        else:
            return None

    def getbwd(self,i):
        k=self.t-1
        c=self.lst
        while k>i:
            k-=1
            c=c.getPrecedent()
        return c

    def inserer(self,i,e):
        k=0
        c=self.fst
        while k<i and c:
            k+=1
            c=c.getSuivant()
        if k==i:
            d=c.getSuivant()
            c.setSuivant(e)
            e.setPrecedent(c)
            e.setSuivant(d)
            if d:
                d.setPrecedent(e)
            else:
                self.lst=e
            self.t+=1

    def __repr__(self):
        s=''
        c=self.fst
        while c:
            s+=' '+str(c.T)
            c=c.getSuivant()
        return s
    
    def recherche(self,v):
        k=0
        c=self.fst
        while c:
            if c.T==v:
                return k
            else:
                k=k+1
                c=c.getSuivant()
        return -1

    def recherchetriee(self,v):
        k=0
        c=self.fst
        while c and c.T<=v:
            if c.T==v:
                return k
            else:
                k=k+1
                c=c.getSuivant()
        return -1

    def insertiontriee(self,e):
        c=self.fst
        while c and c.T<e.T:
            c=c.getSuivant()
        if c:
            d=c.getPrecedent()
            e.setPrecedent(d)
            e.setSuivant(c)
            c.setPrecedent(e)
            if d:
                d.setSuivant(e)
            else:
                self.fst=e
            self.t+=1
        else:
            self.adjq(e)
        
    def maximum(self):
        c=self.fst
        if not c:
            return
        else:
            m=c.T
            while c:
                if c.T>m:
                    m=c.T
                c=c.getSuivant()
            return m

    def __iter__(self):
        self.cur=-1
        return self

    def __next__(self):
        self.cur+=1
        if self.cur<self.t:
            return self.get(self.cur).T
        else:
            raise StopIteration

               
class Cellule:
    def __init__(self,valeur):
        self.T=valeur
        self.suivant=None
        self.precedent=None

    def getElement(self):
        return self.T

    def getPrecedent(self):
        return self.precedent

    def setPrecedent(self,p):
        self.precedent=p

    def getSuivant(self):
        return self.suivant

    def setSuivant(self,s):
        self.suivant=s

if __name__=="__main__":
    l=Liste()
    print(l.taille())
    a,b,c=Cellule(10),Cellule(20),Cellule(30)
    l.adjq(a)
    l.adjq(b)
    l.adjq(c)
    print(l.taille())
    import random
    a=[random.randint(1,100) for k in range(10)]
    l=Liste()
    for k in a:
        l.insertiontriee(Cellule(k))
    print(l.taille())
    print(l)
    for k in range(l.taille()):
        print(l.get(k).getElement(),)
    while l.taille()>0:
        print(l.dernier().getElement())
        l.supprDernier()
    ll=Liste(range(10))
    for k in ll:
        print(k)
