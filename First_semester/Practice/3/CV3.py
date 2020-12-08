#Print sum of all natural numbers smaller or equal import
def sum(n):
    print(int(n*(n+1)/2))

#Print factorial of import
def factorial(n):
    a= 1
    for i in range(1, n+1):
        a= a*i
    print(a)

#Print digit sum of import
def digit_sum(n):
    n= str(n)
    a= 0
    for i in range(len(n)):
        a+= int(n[i])
    print(a)

#Figure out if the imput is prime number
def prime_number(n):
    if(n==1):
        return False
    for i in range(2, int(n**0.5)):
        if(n%i==0):
            return False
    return True

#Print n-number of prime numbers
def prime_numbers(how_many):
    x= 2
    while(how_many>0):
        if(prime_number(x)==True):
            print(x)
            how_many-= 1
        x+= 1

#Print a result of prime factorization of imput
def prime_faktorization(n):
    divisors= []
    j= 2
    for i in range(n):
        if(n%j==0):
            divisors.append(j)
            n= n/j
        else:
            j+= 1
    print(divisors)

#Print greatest common divisor of input numbers
def greatest_common_divisor(a,b):
    while(b!=0):
        c= a%b
        a= b
        b= c
    print(a)

#Return greatest common divisor of input numbers
def gcd(a,b):
    while(b!=0):
        c= a%b
        a= b
        b= c
    return a

#Print least common multiple of input numbers
def least_common_multiple(a,b):
    print(a*b)/gcd(a,b)
