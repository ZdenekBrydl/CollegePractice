#Print all natural numbers smaller and equal the input
def natural_numbers(n):
    for i in range(n):
        print(i+1,'',end= '')

#Print all even numbers smaller and equal the input
def even_numbers(n):
    for i in range(n//2):
        print((i+1)*2,'',end= '')

#Print n - number of second powers of the input
def squares(base, n):
    print('1 ',end = '')
    power= base
    for i in range(n):
        print (power,'',end= '')
        power = power*base

#Print all divisors of the input number
def divisors(n):
    for i in range(n):
        if (n%(i+1)==0):
            print (i+1,'',end= '')

#Print n - number of digits of fibonacci sequence
def fibonacci(n):
    a= 1
    b= 1
    if(n==1):
        print(a,end= '')
    elif(n==2):
        print(a,b,end= '')
    elif(n>0):
        print(a,b,'',end= '')
        for i in range(n-2):
            c= a+b
            print(c,'',end= '')
            a= b
            b= c

#Print square with determinable size
def square(n):
    for i in range(n):
        for j in range(n-1):
            print('# ',end= '')
        print('#')

#Print square sides with determinable size
def empty_square(n):
    for i in range(n):
        if(i==0) or(i==n-1):
            for j in range(n-1):
                print('# ',end= '')
            print('#')
        else:
            print('# ',end = '')
            for k in range(n-2):
                print('  ',end= '')
            print('#')
