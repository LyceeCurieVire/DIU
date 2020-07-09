from heapq import heappush, heappop

class Graphe():
    def __init__(self, matrice_adjacence=None):
        # si la matrice d'adjacence n'est pas donnée
        # on initialise le graphe sans aucun noeud
        self.G=dict()
        self.pds=dict()
        # TODO
        if matrice_adjacence:
            for v,ligne in enumerate(matrice_adjacence):
                voisins=[k for k in range(len(ligne)) if ligne[k]]
                self.G[v]=voisins
    
    def ajouter_noeud(self,u):
    # doit ajouter u  au graphe si celui-ci n'existe pas
    # ne fait rien si il existe déjà
        if u not in self.G:
            self.G[u]=[]

    def noeuds(self):
    # renvoie la liste des noeuds
        return list(self.G.keys())
        

    def ajouter_arete(self,u,v,p=1):
    # ajoute l'arête de u à v
    # on suppose que u et v existent
        self.G[u].append(v)
        self.G[v].append(u)
        self.pds[(u,v)]=p
        self.pds[(v,u)]=p

    def poids(self,u,v):
        return self.pds[(u,v)]

    def enlever_arete(self,u,v):
    # enlève l'arête de u à v
    # ne fait rien si elle n'existe pas
        if v in self.G[u]:
            self.G[u].remove(v)
        if u in self.G[v]:
            self.G[v].remove(u)

    def enlever_noeud(self,u):
    # enlève le noeud u, pour garder la consistence,
    # enlève toutes les arêtes de et vers u
        del self.G[u]
        for e in self.G.values():
            if u in e:
                e.remove(u)

    def voisins(self,u):
    # renvoie la liste des voisins de u
        return self.G[u]

    def nb_sommets(self):
    # renvoie le nombre de sommets
        return len(self.G)

    def nb_aretes(self):
    # renvoie le nombre d'arêtes
        return sum([len(e) for e in self.G.values])//2

    def __str__(self):
    # renvoie une chaîne de caractères représentant
    # le graphe
        s = ""
        for u in self.noeuds():
            s+= "{} -> {}\n".format(str(u),str(self.G[u]))
        return s
        
    def pcc(self,s0,s):
        infini=1000+len(self.G)
        dist=dict()
        pred=dict()
        heap=[]
        heappush(heap,(0,s0))
        for v in self.G.keys():
            dist[v]=infini
            pred[v]=None
        dist[s0]=0
        while heap:
            p,u=heappop(heap)
            for v in self.G[u]:
                if dist[u]+p<dist[v]:
                    dist[v]=dist[u]+p
                    pred[v]=u
                    heappush(heap,(dist[v],v))
        fin=s
        l=[s]
        while pred[fin]:
            l.append(pred[fin])
            fin=pred[fin]
        return l[::-1],dist[s]


    ###########################
    # Q8  complexité en m+n   #
    ###########################
        

    ##################################
    # Q15 complexité en m+n*log(m)   #
    ##################################
        
        

if __name__=="__main__":
# On peut écrire des tests ici, ceux-ci seront executés
# si on appelle ce fichier directement avec python graphe.py
# mais ne le seront pas lors d'un import 
    m=[[0,1,0,0,0],[0,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0],[1,0,0,0,0]]
    graphe=Graphe(m)
    print(graphe)

#############################################
# Question 2                                #
# Avec m=|V| et n=|E|,                      #
# la représentation par matrice est en m**2 #
# et celle par liste en 2*n                 #
# liste d'adjacence pour les graphes peu    #
# denses, pour lesquels n<<m**2             #
#############################################

