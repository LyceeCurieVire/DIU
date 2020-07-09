class tas:

    def __init__(self,l=[]):
        self.t=[0]
        for k in l:
            self.push(k)

    def push(self,e):
        self.t.append(e)
        self.t[0]+=1
        n=self.t[0]
        while n>1:
            if self.t[n]<self.t[n//2]:
                self.t[n//2],self.t[n]=self.t[n],self.t[n//2]
                n=n//2
            else:
                return

    def pop(self):
        if self.vide():
            return
        if self.t[0]==1:
            self.t[0]=0
            return self.t.pop()
        self.t[0]-=1
        e=self.t[1]
        self.t[1]=self.t.pop()
        k=1
        while 2*k+1<=self.t[0]:
            if self.t[k]>min(self.t[2*k],self.t[2*k+1]):
                if self.t[2*k]>self.t[2*k+1]:
                    self.t[k],self.t[2*k+1]=self.t[2*k+1],self.t[k]
                    k=2*k+1
                else:
                    self.t[k],self.t[2*k]=self.t[2*k],self.t[k]
                    k=2*k
            else:
                return e
        if 2*k==self.t[0] and self.t[k]>self.t[2*k]:
            self.t[k],self.t[2*k]=self.t[2*k],self.t[k]
        return e

    def vide(self):
        return self.t[0]==0


if __name__=="__main__":
    hip=tas([15,12,13,18,19,14,17])
    while not hip.vide():
        print(hip.pop())
    import random
    l=[random.randint(1,100) for k in range(10)]
    ta=tas(l)
    ll=[]
    while not ta.vide():
        ll.append(ta.pop())
    print(l)
    
    print(ll)
        
