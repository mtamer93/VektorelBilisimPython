import turtle
import random

# kare çizer
def KareCiz():
    for a in range(4):
        turtle.forward(100)
        turtle.right(90)

# istenilen kenar sayisi kadar cokgen cizer
def SekilCiz(ks = 4):
    for a in range(ks):
        turtle.forward(100)
        turtle.right(360/ks)

# kenar sayısı, uzunlugu, rengi ve baslangic koordinatlari verilen yere cizer
def SekilCiz2(ks = 4, uzunluk = 100, renk = "red", yer_x = 0, yer_y = 0):
    t = turtle.Turtle()
    t.speed(3)
    t.color(renk)
    t.pensize(2)

    t.penup()
    t.goto(yer_x, yer_y)
    t.pendown()

    for _ in range(ks):
        t.forward(uzunluk)
        t.left(360/ks)

    # Birden fazla şekil çizilecekse kapat
    #turtle.done() 

SekilCiz2(6,100,"red",-150,0) # kırmızı 6gen çizer.
SekilCiz2(3,100,"blue",0,0) # mavi üçgen çizer.

# 10 tane rastgele sekil cizer
renkler = ["red", "green", "blue", "purple"]
for a in range(10):
    k = random.randint(3,7)
    b = random.randint(50,200)
    x = random.randint(-300,300)
    y = random.randint(-300,300)

    SekilCiz2(k,b,random.choice(renkler),x,y)

turtle.done()
