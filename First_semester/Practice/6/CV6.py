#Vypis soucet vsech cisel od nuly do vlozeneho cisla
def soucet(a, p= True):
    if(p):
        b= a
        soucetv(b)
        print(" = ",end="")
    #return ((a+1)*a//2) - matematicke reseni bez rekurze
    if(a==1):
        return a
    else:
        return (a+soucet(a-1, False))
def soucetv(b):
    if(b==1):
        print(b,end="")
    else:
        print(b,"+ ",end="")
        soucetv(b-1)
#print(soucet(5))

#Jak funguji rekurze?
def posloupnost(a, p= True):
    if(p):
        b= a
        posloupnostv(b)
        print(" = ",end="")
    if(a==0):
        return 5
    else:
        return (2*posloupnost(a-1, False)-1)
def posloupnostv(b):
    if(b==0):
        print("5",end= "")
    else:
        print("2*(",end= "")
        posloupnostv(b-1)
        print(")-1",end= "")
#print(posloupnost(3))

#Vypis soucet cisel vlozenych v seznamu
def soucet_seznamu(pole):
    if len(pole)<1:
        return 0
    else:
        return (pole[0]+soucet_seznamu(pole[1:]))
#print(soucet_seznamu([1, 8, 2, 0, 4, 2]))

#Vytvor proceduru na reseni Hanoiskych vezi
def hanoi(n, odkud, kam, kudy):
    if(n==1):
        print(odkud,"->",kam)
    else:
        hanoi(n-1, odkud, kudy, kam)
        hanoi(1, odkud ,kam, kudy)
        hanoi(n-1, kudy, kam, odkud)
#hanoi(3, 'A', 'C', 'B')
