import random

class UnionFind():
    def __init__(self):
        self.repr = {}
    def union(self,u,v):
        ru = self.find(u)
        rv = self.find(v)
        self.repr[ru] = rv
    def find(self,u):
        ru = self.repr.get(u)
        if ru is None:
            self.repr[u] = u
            return u
        while ru!=u:
            self.repr[u] = self.repr[ru]
            u = ru
            ru = self.repr[u]
        return ru


"""
test de la classe
"""
if __name__ == "__main__":
    uf = UnionFind()
    N = 20
    for i in range(N):
        for j in range(N):
            uf.find((i,j))
    for i in range(N//2):
        n1,n2 = random.randint(0,N), random.randint(0,N)
        uf.union(n1,n2)
        print(" union {} {}".format(n1,n2))

    for i in range(N):
        for j in range(N):
            print("{} ".format(uf.find(i)==uf.find(j)),end="")
        print()
