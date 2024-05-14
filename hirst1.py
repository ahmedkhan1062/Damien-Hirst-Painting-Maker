import random, turtle, colorgram
from turtle import Turtle, Screen

turtle.colormode(255)
turd = Turtle()
turd.width(2)
turd.shape("turtle")
turd.speed("fastest")
colours = colorgram.extract('damien.jpg',15)
newcol = []
for i in colours:
    cat = (i.rgb.r, i.rgb.g, i.rgb.b)
    newcol.append(cat)

print(newcol)


def printColour(color):
    turd.pencolor(color)
    turd.fillcolor(color)
    turd.begin_fill()
    turd.circle(10)
    turd.end_fill()


turd.penup()
turd.setx(-200)
turd.sety(100)
turd.pendown()


for y in range(8):

    #printColour(random.choice(newcol))
    turd.penup()
    turd.right(90)

    for j in range(6):


       # turd.setx(-200)



        turd.pendown()
        printColour(random.choice(newcol))
        turd.penup()
        turd.forward(60)
    turd.left(90)

    #turd.penup()
    turd.forward(60)
    turd.sety(100)
    turd.pendown()



screen = Screen()
screen.exitonclick()

