#Print n - numbers of didgets of consecutive sequences starting from one and gradually increasing by one
def sequences(n):
    b= 1
    c= 1
    while(b<=n):
        for i in range(c):
            if(b<=n):
                print(i+1,'',end = '')
            b= b+1
        print()
        c= c+1

#Print n - number of layers of pyramid
def pyramid(n):
    a= n-1
    for i in range(n):
        for space in range(a):
            print(' ',end = '')
        a= a-1
        for block in range((i+1)*2-1):
            print('#',end = '')
        print()

#Print a picture of n - number of nested squares
def nested_squares(n):
    size= 1+4*(n-1) #size is a parameter for size of the outermost square
    for y in range(size):
        yh= y-size//2
        for x in range(size-1):
            xh= x-size//2
            if((xh%2==0) and(abs(xh)>=abs(yh))) or((yh%2==0) and(abs(yh)>=abs(xh))):
                print('# ',end = '')
            else:
                print('  ',end = '')
        print('#')
def nested_squares2(n):
    for y in range(-2*n+2, 2*n-1):
        for x in range(-2*n+2, 2*n-1):
            if(max (abs(x), abs(y))%2==0):
                print('# ',end = '')
            else:
                print('  ',end = '')
        print()
#Without if
def nested_squares3(n):
    for y in range(-2*n+2, 2*n-1):
        for x in range(-2*n+2, 2*n-1):
            print(chr(35-3*(max(abs(x), abs(y))%2))+' ',end = '')
        print()
