import turtle
from turtle import *
from math import sqrt
turtle.speed(10)
left(90)
turtle.tracer(1, 0)
#Vykresli dany pocet ctvercu, dy stredni pricky jednoho jsou stranami dalsiho
def ctverce(delka, zanoreni):
    if(zanoreni!=0):
        for i in range(4):
            forward(delka)
            left(90)
        forward(delka/2)
        left(45)
        ctverce(sqrt(delka*delka/2), zanoreni-1)
#ctverce(100, 5)
#Vykresli strom vetvici se tolikrat, kolikrat se zada - chybel jsem a dodelaval doma z hlavy!>>>
def tree(kmen, zanoreni):
    if(zanoreni!=0):
        forward(kmen)
        left(45)
        tree(kmen/1.4, zanoreni-1)
        right(90)
        tree(kmen/1.4, zanoreni-1)
        left(45)
        backward(kmen)
#tree(100,10)
#Vykresli vlocku s danou slozitosti jednostlivych vetvi a i poctem vetvi - chybel jsem a dodelaval doma z hlavy!>>>
def vlocka(delka,zanoreni,vetve):
    for n in range(vetve):
        tree(delka, zanoreni)
        right(360/vetve)
turtle.update()
vlocka(100,10,10)
