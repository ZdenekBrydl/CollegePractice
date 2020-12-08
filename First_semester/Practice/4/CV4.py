import random
from random import randint

#Vytvoř daný počet náhodných čísel s horním a spodním limitem, vypiš nejmenší a největší vytvořené číslo a průměr všech
def statistiky(pocet, spodni_mez=0, horni_mez=100):
    a= []
    nm= spodni_mez
    nv= horni_mez
    for i in range(pocet):
        a.append(randint(spodni_mez, horni_mez))
        if(nm<a[i]):
            nm= a[i]
        if(nv>a[i]):
            nv= a[i]
    print("minimum",nm)
    print("maximum",nv)
    print("prumer:",sum(a)/(i + 1))

#Simuluj cestu opilce domů s možností zabloudění do hosody
def simulace_opilce(delka, pocet_kroku, vypis= True):
    pozice= delka//2
    konec= "doma "+delka*" . "+" hospoda"  
    if(vypis): print("doma",(pozice)*" . ","*",(delka-pozice-1)*" . ","hospoda")
    for x in range(pocet_kroku):
        pozice+= random.choice([-1, 1])
        if(pozice==-1):
            if(vypis): print(konec,"\nDosel dom")
            else: return True
            break
        if(pozice==delka):
            if(vypis): print(konec,"\nDosel do hospody")
            else: return False
            break
        if(vypis): print("doma",(pozice)*" . ","*",(delka-pozice-1)*" . ","hospoda")
    else:
        if(vypis): print("Usnul na ceste")
        else: return False

#Vypiš percentuelní úspěšnost opilce při cestě domů
def analyza_opilce(pocet_pokusu, delka, pocet_kroku):
    uspesne= 0
    for i in range(pocet_pokusu):
        if simulace_opilce(delka, pocet_kroku, vypis= False):
            uspesne+= 1
    print(float(uspesne)/pocet_pokusu*100,"%")
