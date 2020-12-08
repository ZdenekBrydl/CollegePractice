#Procedura tvorici posloupnost pri vstupu 10: 7  1  14  1  21  1  28  1  35 1
def 1posloupnost(n):
    a= 1 
    for i in range((n//2)+(n%2)):
        print(7*(i+1)," ",end= "")
        a= a+1
        if(a<=n):
            print(1," ",end= "")
            a= a+1
#Procedura tvorici posloupnost pri vstupu 10: 1  2  2  4  8  32  56  92  52  84
def 2posloupnost(n):
    a= 1
    b= 2
    print(a," ",end= "")
    for i in range(n-1):
        print(b," ",end= "")
        c= b
        b= (a*b)%100
        a= c
#Procedura tvorici posloupnost pri vstupu 100: 8  16  32  40  56  64  80  88
def 3posloupnost1(n):
    a= 0
    for i in range(n):
        a= a+8
        if(a>n):
            break
        if (a%8==0) and(a%3!=0):
            print(a," ",end= "")
def 3posloupnost2(n):
    for i in range(n//8+1):
        if (i%3!=0):
            print(8*i," ",end= "")
#Vykresli obdelnik o staranach danych na vstupu
def obdelnik(a, b):
    for i in range(a-1):
        print("# ",end= "")
    print("#")
    for i in range(b-2):
        print("# ",end= "")
        for i in range(a-2):
            print(". ",end= "")
        print("#")
    for i in range(a-1):
        print("# ",end= "")
    print("#")
#Vykresli diamant o velikosti dane na vstupu
def diamant1(n):
    a= n-1
    b= 1
    for i in range(n):
        for mezera in range(a):
            print('  ',end= "")
        a= a-1
        for znak in range((i+1)*2-2):
            print('# ',end= "")
        print('#')
    i= i-1
    for j in range(n-1):
        for mezera in range(b):
            print('  ',end= "")
        b= b+1
        for znak in range((i+1)*2-2):
            print ('# ',end= "")
        i= i-1
        print('#')
def diamant2(n):
    for i in range(n):
        for j in range(n-i-1):
            print('  ',end= "")
        for j in range(2*i):
            print('# ',end= "")
        print('#')
    for i in range(n-1):
        for j in range(i+1):
            print('  ',end= "")
        for j in range(2*(n-i)-4):
            print('# ',end= "")
        print('#')
def diamant3(n):
    for i in range(2*n-1):
        for j in range(abs(n-i-1)):
            print('  ',end= "")
        for j in range(2*(n-abs(n-i-1))-2):
            print('# ',end= "")
        print('#')
