
def edit(u,v):
    if u=='' or v=='':
        return max(len(u),len(v))
    elif u[-1]==v[-1]:
        return edit(u[:-1],v[:-1])
    else:
        a=edit(u[:-1],v)
        b=edit(u,v[:-1])
        c=edit(u[:-1],v[:-1])
        return(1+min(a,b,c))

def recherche_naive(t,x):
    n,m=len(t),len(x)
    p=[]
    for i in range(n-m):
        j=m-1
        while j>=0 and x[j]==t[i+j]:
            j=j-1
        if j==-1:
            p.append(i)
    return(p)
                   
       
    

if __name__=='__main__':
    print(edit('pecheurs','ecriture'))
    print(edit('ALGORITHME','POLYRYTHMIE'))
    print(recherche_naive('acaabbabaaa','abaa'))
