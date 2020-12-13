from random import randint
#Vytvoř hru nepodobující piškvorky v jedné dimenzi
def piskvorky():
    #zadání hry:
    plan= int(input("Zadej velikost plánu: "))
    #kontrola velikosti plánu:
    while((plan<5)or(plan>50)):
        if(plan<5):
            plan= int(input("Zadej vyšší hodnotu: "))
        else:
            plan= int(input("Zadej nižší hodnotu: "))
    zacina_hrac= int(input("Zadej 1 pro to, aby jsi začínal ty, nebo 0, aby začínal počítač: "))
    #kontrola začínajícího hráče:
    while((zacina_hrac!=0)and(zacina_hrac!=1)):
        zacina_hrac= int(input("!1! pro to, abys začínal ty, !0! aby začínal počítač: "))
    uroven_AI= int(input("Zadej úroveň inteligence počítače, 1 pro nejhloupějšího, 2 je pro průměrného a 3 pro nejchytřejšícho: "))
    #kontrola úrovně inteligence:
    uroven_debility= 0
    while((uroven_AI!=1)and(uroven_AI!=2)and(uroven_AI!=3)):
        uroven_AI= int(input("!1! pro nejhloupějšího, !2! pro průměrného, !3! pro nejchytřejšícho: "))
        uroven_debility+= 1
        if(uroven_debility>1):
            print("Všechny tři umělé inteligence se shodli na tom, že s takovým idiotem hrát nechtějí.")
            return "Idiot"
    #seznam plánu:
    hra_plan= []
    for i in range(plan):
        hra_plan.append(0)
    #vykreslení plánu:
    vykresli_plan(hra_plan)
    #hra:
    while(konec(hra_plan)):
        #tah hráče:
        if(zacina_hrac==1):
            tah_hrac(hra_plan, int(input("Zadej tah: ")))
            zacina_hrac=False
        #tah počítače:
        else:
            if(uroven_AI==1):
                tah_pocitac1(hra_plan)
            if(uroven_AI==2):
                tah_pocitac2(hra_plan)
            if(uroven_AI==3):
                tah_pocitac3(hra_plan, 0)
            zacina_hrac= True
        vykresli_plan(hra_plan)
    #konec hry:
    else:
        if(zacina_hrac):
            print("Prohrál jsi")
        else:
            print("Vyhrál jsi")
#Procedura na vykreslení hracího plánu:
def vykresli_plan(hra_plan):
    i= 0
    for j in range(len(hra_plan)):
        if(hra_plan[j]==0):
            print("_",end="")
        else:
            print("X",end="")
    print()
    for k in range(len(hra_plan)):
        if(k>9):
            k%= 10
        print(k,end="")
    print()
    for l in range(len(hra_plan)//10):
        for l in range(4):
            print(" ",end="")
        print(i,end="")
        for l in range(4):
            print(" ",end="")
        print("|",end="")
        i+= 1
    print()
    return 0
#Procedura pro tah hráče:
def tah_hrac(hra_plan, pozice):
    if(pozice<len(hra_plan)):
        if(pozice>=0):
            if(not(zabrane_policko(hra_plan, pozice))):
                del hra_plan[pozice]
                hra_plan.insert(pozice, 1)
            else:
                print("Políčko je zabrané")
                tah_hrac(hra_plan, int(input("Zadej tah: ")))
        else:
            print("Políčko tak nízkého čísla zde není")
            tah_hrac(hra_plan, int(input("Zadej tah: ")))
    else:
        print("Políčko tak vysokého čísla zde není")
        tah_hrac(hra_plan, int(input("Zadej tah: ")))
#Procedury pro tah počítače:
#AI 1:
def tah_pocitac1(hra_plan):
    pozice= (randint (0, len(hra_plan)-1))
    if(not(zabrane_policko(hra_plan, pozice))):
        print ("Počítač hraje na pozici:", pozice)
        del hra_plan[pozice]
        hra_plan.insert(pozice, 1)
    else:
        tah_pocitac1(hra_plan)
#AI 2:
def tah_pocitac2(hra_plan):
    #otázka: je možné dosáhnout vítězství?
    if(vitezstvi(hra_plan)):
        pozice= (vitezstvi_cislo(hra_plan))
    else:
        pozice= (randint (0, len(hra_plan)-1))
    if(not(zabrane_policko(hra_plan, pozice))):
        print ("Počítač hraje na pozici:", pozice)
        del hra_plan[pozice]
        hra_plan.insert(pozice, 1)
    else:
        tah_pocitac2(hra_plan)
#AI 3:
def tah_pocitac3(hra_plan, a):
    n=0
    #otázka: je možné dosáhnout vítězství?
    if(vitezstvi(hra_plan)):
        pozice= (vitezstvi_cislo(hra_plan))
        n=1
    else:
        pozice= (randint (0, len(hra_plan)-1))
    if(n==0):
        if(not(zabrane_policko(hra_plan, pozice))):
            #otázka: je okolo zabrané políčko? (nenahrávat protivníkovi)
            if(zabrane_policko_okolo(hra_plan, pozice)):            
                print("Počítač hraje na pozici:", pozice)
                del hra_plan[pozice]
                hra_plan.insert(pozice, 1)
            elif(a<=len(hra_plan)):
                a+= 1
                tah_pocitac3(hra_plan, a)
            else:
                b= 0
                while(b!=1):
                    pozice= (randint (0, len(hra_plan)-1))
                    if(not(zabrane_policko(hra_plan, pozice))):
                        print("Počítač hraje na pozici:", pozice)
                        del hra_plan[pozice]
                        hra_plan.insert(pozice, 1)
                        b= 1
        elif(a<= len(hra_plan)):
            a+= 1
            tah_pocitac3(hra_plan, a)
        else:
            b= 0
            while(b!=1):
                pozice= (randint (0, len(hra_plan)-1))
                if(not(zabrane_policko(hra_plan, pozice))):
                    print("Počítač hraje na pozici:", pozice)
                    del hra_plan[pozice]
                    hra_plan.insert(pozice, 1)
                    b= 1
    else:
        print("Počítač hraje na pozici:", pozice)
        del hra_plan[pozice]
        hra_plan.insert(pozice, 1)
#Procedura pro zjištění zdali již není hra u konce
def konec(hra_plan):
    for i in range(len(hra_plan)):
        if((i+2<len(hra_plan)and(hra_plan[i]==1)and(hra_plan[i+1]==1)and(hra_plan[i+2]==1))):
           return False
    return True
#Procedura pro zjištění zdali vybraná pozice není zabraná
def zabrane_policko(hra_plan, pozice):
    if(hra_plan[pozice]==1):
        return True
    return False
#Procedura pro zjištění zdali je možné vyhrát
def vitezstvi(hra_plan):
    for i in range(len(hra_plan)):
        if(hra_plan[i]==1):
            i+= 1
            if(i<len(hra_plan)):
                if(hra_plan[i]==1):
                    return True
                elif(hra_plan[i+1]==1):
                    return True
            else:
                return False
#Procedura pro zjištění vítězného tahu
def vitezstvi_cislo(hra_plan):
    for i in range(len(hra_plan)):
        if(hra_plan[i]==1):
            i+= 1
            if(hra_plan[i]==1):
                if(i+1<len(hra_plan)):
                    return (i+1)
                if(i-2>=0):
                    return (i-2)
            elif(hra_plan[i+1]==1):
                return (i)
#Procedura pro zjištění jestli AI svým tahem umožní hráči vyhrát
def zabrane_policko_okolo(hra_plan, pozice):
    if(pozice-2<0):
        if(pozice-1<0):
            if(hra_plan[pozice+1]==1)or(hra_plan[pozice+2]==1):
                return False
        elif(hra_plan[pozice-1]==1)or(hra_plan[pozice+1]==1)or(hra_plan[pozice+2]==1):
            return False
    elif(pozice+1>=len(hra_plan)-1):
        if(pozice>=len(hra_plan)-1):
            if(hra_plan[pozice-1]==1)or(hra_plan[pozice-2]==1):
                return False
        elif(hra_plan[pozice+1]==1)or(hra_plan[pozice-1]==1)or(hra_plan[pozice-2]==1):
            return False
    elif(hra_plan[pozice+1]==1)or(hra_plan[pozice+2]==1)or(hra_plan[pozice-1]==1)or(hra_plan[pozice-2]==1):
        return False
    return True

piskvorky()
