"""
import turtle

def escalier(taille,nb):
    for i in range(0,nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)

t=turtle.Turtle()

escalier(60,10)
turtle.done()
"""
import turtle
def carre(taille):
    for i in range(0,4):
        t.forward(taille)
        t.left(90)

def carres(taille_de_depart,nb):
    for i in range(0,nb):
        taille=(i+1)*taille_de_depart
        carre(taille)

t=turtle.Turtle()
carres(10,10)
turtle.done()
