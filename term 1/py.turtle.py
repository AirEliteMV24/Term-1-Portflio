#Max Virkus
#10/11
#Turtle Drawings

from turtle import *
import turtle
t = turtle.Turtle()
Window = turtle.Screen()

Window.bgcolor('white')

turtle.color('white')
goto(-200, -200)
def serp_tri(side, level):
    if level == 1:
        for i in range(3):
            turtle.color('black')
            turtle.ht()
            turtle.fd(side)
            turtle.left(120)
            turtle.speed(100000)
    else:
        turtle.ht()
        serp_tri(side/2, level-1)
       turtle.fd(side/2)
         serp_tri(side/2, level-1)
        turtle.bk(side/2)
    turtle.left(60)
    turtle.fd(side/2)
    turtle.right(60)
    serp_tri(side/2, level-1)
    turtle.left(60)
    turtle.bk(side/2)
    turtle.right(60)
    turtle.speed(100000)

def main():
    serp_tri(400, 8)

if __name__ == '__main__':
    main()
    turtle.mainloop()

