from random import random, randint
#Vytvor jednoduchou hru clovece nezlob se o jedne postavicce s kruhovym hracim polem a preskocitelnym cilem
def hra_clovece(pocet_poli, vypis=True):
    pocet_kol= 0
    licha= 0
    hod= 0
    pozice= 0
    kolo= 0
    while(pocet_poli!=pozice):
        kolo+= 1
        if(licha%2==1):
            hod= randint(1,4)
            while(hod%4==0):
                hod+= randint(1,4)
        else:
            hod= randint(1,8)
            while(hod%8==0):
                hod+= randint(1,8)
        pozice+= hod
        if vypis:
            print("kolo", kolo, ", hod", hod)
            if (pocet_poli<pozice):
                print("od znova")
            if(pocet_poli >= pozice):
                print("pozice:", pozice)
            else:
                print("pozice:", pozice%pocet_poli )
        if(pocet_poli < pozice):
            pozice= 0+(pozice%pocet_poli)
    pocet_kol+= kolo
    if vypis:
        print("hra dokoncena v", kolo, ". kole")
    else:
        return pocet_kol
#Vytvor proceduru pocitajici prumerny pocet kol potrebnych k dokonceni hry
def analyza_clovece(pocet_poli, pocet_opakovani):
    pocet_kol= 0
    if(pocet_poli>1):
        if(pocet_poli<50):
            for i in range(pocet_opakovani):
                hra_clovece(pocet_poli, vypis=False)
                pocet_kol+= (hra_clovece(pocet_poli, vypis=False))
            print("prumerny pocet kol:", (float(pocet_kol)/float(pocet_opakovani)))
        else:
            print("prumerny pocet kol:", 0.0)
    else:
        print("prumerny pocet kol:", 0.0)
    

    
