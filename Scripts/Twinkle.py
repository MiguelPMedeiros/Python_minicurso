from musica_piano import *
def P1():
    sol3.toca(1)
    sol3.toca(1)
    re.toca(1)
    re.toca(1)
def P2():
    mi.toca(1)
    mi.toca(1)
    re.toca(2)
def P3():
    do.toca(1)
    do.toca(1)
    si3.toca(1)
    si3.toca(1)
def P4():
    la3.toca(1)
    la3.toca(1)
    sol3.toca(1)
def P5():
    re.toca(1)
    re.toca(1)
    do.toca(1)
    do.toca(1)
    si3.toca(1)
    si3.toca(1)
    la3.toca(2)
def Musica():
    for i in range(2):
        P1()
        P2()
        P3()
        P4()
        for i in range(2):
            P5()
        P1()
        P2()
        P3()
        P4()
#def acorde():
   # do.tocafade(4)
    #mi.tocafade(4)
    #sol.tocafade(4)
Musica()
#acorde()
