from turtle import *

pencolor("deepskyblue")
fillcolor("silver")
begin_fill()
bgcolor("black")
speed = 100

sides = 5
distance = 100
for _ in range(50*sides):
    distance += 20
    forward(distance)
    right(2*360.0/sides+1)

begin_fill()
fillcolor("silver")
speed=100
pencolor("silver")

sides=5
distance = 50
for _ in range(25*sides):
    distance += 10
    forward(distance)
    right(2*180/sides+1)

end_fill()
