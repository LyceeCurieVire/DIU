# plus longue sous suite commune / alignement
# le dict plssc[(i,j)] contient la longueur de la plssc entre s[:i] et t[:j]



def construitPLSSC(s,t):
    pl=dict()
    for i in range(len(s)+1):
        pl[(i,0)]=0
    for j in range(len(t)+1):
        pl[(0,j)]=0
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            #print((i,j))
            #print(pl)
            #assert (i-1,j-1) in pl
            #assert (i-1,j) in pl
            #assert (i,j-1) in pl
            pl[(i,j)]=pl[(i-1,j-1)]+1 if s[i-1]==t[j-1] else max(pl[(i-1,j)],pl[(i,j-1)])
    return pl

def PLSSC(s,t):
    pl=construitPLSSC(s,t)
    i,j=len(s),len(t)
    u=''
    while pl[(i,j)]>0:
        if pl[(i,j)]==pl[(i-1,j)]:
            i=i-1
        elif pl[(i,j)]==pl[(i,j-1)]:
            j=j-1
        else:
            u=s[i-1]+u
            i=i-1
            j=j-1
    return(u)
    

if __name__=='__main__':
    s,t='TASTASPE','ARSENIC'
    plssc=construitPLSSC(s,t)
    print(plssc[(len(s),len(t))])
    print(PLSSC(s,t))
    print(PLSSC('abracdadabracadrabaabbacadabacab','abba'))
    
