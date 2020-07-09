# Karatsuba
# (a*10**k+b)(c*10**k+d)=ac*10**(2*k)+(ac+bd-(a-b)(c-d))*10**2k+bd

def cmp(u,v):
    """
    renvoie u<=v
    """
    if len(v)>len(u):
        return True
    if len(u)>len(v):
        return False
    n=len(u)-1
    while n>0 and u[n]==v[n]:
        n-=1
    return u[n]<=v[n]

def add(u,v):
    i=0
    s=[]
    r=0
    if len(u)>len(v):
        v+=[0]*(len(u)-len(v))
    elif len(v)>len(u):
        u+=[0]*(len(v)-len(u))
    while i<len(u) and i <len(v):
        c=u[i]+v[i]+r
        s.append(c%10)
        r=c//10
        i+=1
    if r>0:
        s.append(r)
    return(s)

def sub(u,v):
    assert cmp(v,u)
    v+=[0]*(len(u)-len(v))
    r=0
    d=[]
    for i in range(len(u)):
        c=u[i]-v[i]-r
        if c<0:
            c+=10
            r=1
        else:
            r=0
        d.append(c)
    return d
    

def k2d(u):
    n=0
    for k in u[::-1]:
        n=n*10+k
    return n

def d2k(n):
    u=[]
    while n>0:
        u.append(n%10)
        n=n//10
    return u

def nul(u):
    return u==[0] or u==[]

def karatsuba(u,v):
    print(k2d(u),k2d(v),u,v)
    if nul(u) or nul(v):
        return [0]
    if len(v)>len(u):
        u,v=v,u
    n=len(u)
    if n==1:
        p=u[0]*v[0]
        return [p%10,p//10] if p>=10 else [p]
    k=n//2
    a,b,c,d=u[k:],u[:k],v[k:],v[:k]
    ac=karatsuba(a,c)
    bd=karatsuba(b,d)
    sgn=False
    if cmp(a,b):
        x=sub(b,a)
        sgn=not sgn
    else:
        x=sub(a,b)
    if cmp(c,d):
        y=sub(d,c)
        sgn=not sgn
    else:
        y=sub(c,d)
    xy=karatsuba(x,y)
    z=add(ac,bd)
    if sgn:
        t=add(z,xy)
    else:
        t=sub(z,xy)
    p=add([0]*k+ac,t)
    return add([0]*k+p,bd)


if __name__=='__main__':
    u=[1,9,2]
    v=[8,8]
    print(add(u,v))
    print(sub(u,v))
    print(karatsuba(u,v))
    u=d2k(2**32-1)
    v=d2k(2**64-1)
    w=karatsuba(u,v)
    print(k2d(w), (2**32-1)*(2**64-1))
