"""
Implementacni test IB002

Vyplnte nasledujici udaje:
Jmeno: ZDENEK BRYDL
UCO: XXXXXX
Skupina (do ktere jste zapsani): XXXXXX
"""

"""
Jednostranne spojovany seznam znate z prednasky - jde o zretezeny seznam
uzlu (Node), kde kazdy uzel ukazuje na sveho naslednika. 

Tato uloha pracuje se dvema typy jednostranne spojovanych seznamu:
Linearni seznam - kde posledni prvek seznamu ukazuje na None. 
Kruhovy seznam - kde posledni prvek seznamu ukazuje zpet na prvni prvek seznamu.

Vasim ukolem je naprogramovat nasledujici funkce:

1) getLength: zjisti delku (tj. pocet ruznych uzlu) seznamu

2) isCircular: otestuje, zda je seznam kruhovy

3) calculateOpposites: pro kruhove seznamy delky 2n naplni u kazdeho uzlu
polozku opposite uzlem, ktery je o n kroku dale (tedy v kruhu je to uzel
"naproti"). Napriklad v kruhovem seznamu 1 -> 2 -> 3 -> 4 (-> 1) je opposite
uzlu 1 uzel 3, uzlu 2 uzel 4, uzlu 3 uzel 1 a uzlu 4 uzel 2.

Pro vsechny funkce muzete predpokladat, ze seznam na vstupu obsahuje
vzajemne ruzne klice a ze je linearni nebo kruhovy, tj. nemusite napriklad
osetrovat situaci, kdy naslednikem "posledniho" v seznamu je "druhy".

Chovani funkce calculateOpposites neni definovano na kruhovem seznamu liche
(neparne) delky. Tento pripad nebude testovan, nemusite jej tedy overovat.
"""

"""
Trida Node reprezentujici prvek v spojovanem seznamu
"""
class Node:
    def __init__(self): 
        self.key = 0         # klic
        self.next = None     # dalsi prvek seznamu
        self.opposite = None # protejsi prvek seznamu

"""
Doprogramujte nasledujici funkce
"""

"""
Otestuje, zda je zadany zretezeny seznam kruhovy.

Prazdny seznam neni kruhovy.

@param node: prvni uzel seznamu

@ret: True pokud je seznam kruhovy, False jinak
"""
def isCircular(node):
    prvni_uzel = node
    while node.next != prvni_uzel and node.next != None:
        node = node.next
    if node.next == prvni_uzel:
        return True
    return False

"""
 Vrati delku (linearniho nebo kruhoveho) zretezeneho seznamu zacinajiciho
v zadanem uzlu. 

Pokud je seznam prazdny, vrati 0.

@param node: prvni uzel seznamu

@ret: delka (pocet prvku) seznamu,  0 pokud je prazdny (None)
"""
def getLength(node):
    prvni_uzel = node
    i = 1
    if node == None:
        return 0
    while node.next != prvni_uzel and node.next != None:
        node = node.next
        i += 1
    return i

"""
Korektne naplni polozky "opposite" v uzlech kruhoveho seznamu sude
delky.

Pokud vstupni seznam neni kruhovy nebo nema sudou delku (neni testovano,
nemusite osetrovat), nedela nic, tj. seznam neupravuje.

@param node: prvni uzel seznamu 
"""
def protejsi (node, delka):
    for i in range(delka):
        node = node.next
    return node

def calculateOpposites(node):
    if not isCircular(node):
        return    
    prvni_uzel = node
    delka = getLength(node)
    control = False
    if delka % 2 != 0:
        return
    while node != prvni_uzel or not control:
        control = True
        node.opposite = protejsi(node, delka // 2)
        node = node.next                
    pass
    
"""
Nasledujuce funkce slouzi na testovani, nemente je.
"""
    
"""
Vytvori jednosmerne spojovany seznam z danych hodnot

@param l: vstupni hodnoty (obycejny seznam)

@ret: prvni uzel vytvoreneho seznamu        
"""
def makeLinkedList(l):
    fakeStart = Node()
    tmp = fakeStart
    for x in l:
        n = Node()
        n.key = x
        tmp.next = n
        tmp = n
    return fakeStart.next

"""
Vytvori kruhovy, jednosmerne spojovany seznam z danych hodnot

@param l: vstupni hodnoty (obycejny seznam)

@ret: prvni uzel vytvoreneho seznamu        
"""
def makeCircularList(l):
    fakeStart = Node()
    tmp = fakeStart
    for x in l:
        n = Node()
        n.key = x
        tmp.next = n
        tmp = n
    tmp.next=fakeStart.next
    return fakeStart.next

"""
Testuje, zda protejsi prvky seznamu zacinajiciho danym uzlem maji dane klice

@param node: prvni uzel seznamu
@param olist: seznam klicu

@ret: True pokud maji protejsi prvky klice z daneho seznamu, False jinak
"""
def testOpposites(node, olist):
    tmp = node
    for o in olist:
        if(tmp.opposite == None):
            return False
        if (o != tmp.opposite.key):
            return False
        else:
            tmp = tmp.next
    return True


# Testovaci kod
print("Test 1: delka prazdneho seznamu")
node = makeLinkedList([])
if getLength(node) == 0:
    print("PASSED")
else:
    print("FAILED!, melo byt 0, vase delka je " + str(getLength(node)))

###
print("")
print("Test 2a: seznam delky 2, nekruhovy - delka")
node = makeLinkedList([4, 8])
if getLength(node) == 2:
    print("PASSED")
else:
    print("FAILED!, melo byt 2, vase delka je " + str(getLength(node)))

print("Test 2b: seznam delky 2, nekruhovy - kruhovost")
if not isCircular(node):
    print("PASSED")
else:
    print("FAILED!, oznacili jste nekruhovy seznam za kruhovy")

print("Test 2c: seznam delky 2, nekruhovy - protejsky")
calculateOpposites(node)
if node.opposite == None:
    print("PASSED")
else:
    print("FAILED!, nekruhovy seznam nema protejsky")

###
print("")
print("Test 3a: seznam delky 2, kruhovy - delka")
node = makeCircularList([4, 8])
if getLength(node) == 2:
    print("PASSED")
else:
    print("FAILED!, melo byt 2, vase delka je " + str(getLength(node)))

print("Test 3b: seznam delky 2, kruhovy - kruhovost")
if isCircular(node):
    print("PASSED")
else:
    print("FAILED!, oznacili jste kruhovy seznam za nekruhovy")

print("Test 3c: seznam delky 2, kruhovy - protejsky")
calculateOpposites(node)
if testOpposites(node, [8,4]):
    print("PASSED")
else:
    print("FAILED!, kruhovemu seznamu jste nastavili spatne protejsky:")
    print("nasledujici vypis by mel vypadat takto 4->8, 8->4,")
    tmp = node
    for i in range(0,2):
        if(tmp != None):
            if(tmp.opposite != None):
                print(tmp.key,"->",tmp.opposite.key,)
            else:
                print(tmp.key,"->None,"),
        tmp = tmp.next
    print("")
###

print("")
print("Test 4a: seznam delky 6, nekruhovy - delka")
node = makeLinkedList([3, 5, 6, 7, 9, 10])
if getLength(node) == 6:
    print("PASSED")
else:
    print("FAILED!, melo byt 6, vase delka je " + str(getLength(node)))

print("Test 4b: seznam delky 6, nekruhovy - kruhovost")
if not isCircular(node):
    print("PASSED")
else:
    print("FAILED!, oznacili jste nekruhovy seznam za kruhovy")

print("Test 4c: seznam delky 6, nekruhovy - protejsky")
calculateOpposites(node)
if node.opposite == None:
    print("PASSED")
else:
    print("FAILED!, nekruhovy seznam nema protejsky")

###
print("")
print("Test 5a: seznam delky 6, kruhovy - delka")
node = makeCircularList([3, 5, 6, 7, 9, 10])
if getLength(node) == 6:
    print("PASSED")
else:
    print("FAILED!, melo byt 6, vase delka je " + str(getLength(node)))

print("Test 5b: seznam delky 6, kruhovy - kruhovost")
if isCircular(node):
    print("PASSED")
else:
    print("FAILED!, oznacili jste kruhovy seznam za nekruhovy")

print("Test 5c: seznam delky 6, kruhovy - protejsky")
calculateOpposites(node)
if testOpposites(node, [7, 9, 10, 3, 5, 6]):
    print("PASSED")
else:
    print("FAILED!, kruhovemu seznamu jste nastavili spatne protejsky:")
    print("nasledujici vypis by mel vypadat takto 3->7, 5->9, 6->10, 7->3, 9->5, 10->6,")
    tmp = node
    for i in range(0,6):
        if(tmp != None):
            if(tmp.opposite != None):
                print(tmp.key,"->",tmp.opposite.key,)
            else:
                print(tmp.key,"->None,"),
        tmp = tmp.next
    print("")


