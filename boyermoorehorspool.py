# Boyer Moore Horspool

def naive(texte,motif):
    for i in range(len(texte)-len(motif)+1):
        if texte[i:i+len(motif)]==motif:
            return i
    return -1


def naivewhile(texte,motif):
    i=0
    while i+len(motif)<=len(texte):
        j=0
        while j<len(motif):
            if texte[i+j]==motif[j]:
                j+=1
            else:
                break
        if j==len(motif):
            return(i)
        else:
            i+=1
    return(-1)

def naiveback(texte,motif):
    i=0
    while i+len(motif)<=len(texte):
        j=len(motif)-1
        while j>=0:
            if texte[i+j]==motif[j]:
                j-=1
            else:
                break
        if j<0:
            return(i)
        else:
            i+=1
    return(-1)


def bmh(texte,motif):
    # construit le dict de saut
    saut=dict()
    for i,c in enumerate(motif[:-1]):
        saut[c]=len(motif)-i-1    
    i=0
    while i+len(motif)<=len(texte):
        j=len(motif)-1
        while j>=0:
            if texte[i+j]==motif[j]:
                j-=1
            else:
                if texte[i+j] in saut:
                    i+=saut[texte[i+j]]
                else:
                    i+=len(motif)
                break
        if j<0:
            return(i)
    return(-1)





if __name__=='__main__':
    print(naive('carambar','mba'))
    print(naive('carambar','abba'))
    print(naive('abracacdacearcabrabaddacabra','acab'))
    print(naive('abracacdacearcabrabaddacabra','bac'))


    print(naivewhile('carambar','mba'))
    print(naivewhile('carambar','abba'))
    print(naivewhile('abracacdacearcabrabaddacabra','acab'))
    print(naivewhile('abracacdacearcabrabaddacabra','bac'))
    
    print(naiveback('carambar','mba'))
    print(naiveback('carambar','abba'))
    print(naiveback('abracacdacearcabrabaddacabra','acab'))
    print(naiveback('abracacdacearcabrabaddacabra','bac'))

    print(bmh('carambar','mba'))
    print(bmh('carambar','abba'))
    print(bmh('abracacdacearcabrabaddacabra','acab'))
    print(bmh('abracacdacearcabrabaddacabra','bac'))



    
