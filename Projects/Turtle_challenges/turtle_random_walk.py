from random import choice,randrange
from turtle import Screen,Turtle,colormode

turtle = Turtle()
colormode(255)

def rand_colour():
    r = randrange(0,255)
    g = randrange(0,255)
    b = randrange(0,255)
    color = (r,g,b)
    return color

direction = [0,90,180,270]
turtle.width(15)
turtle.speed(0)

for i in range(200):
    turtle.pencolor(rand_colour())
    turtle.forward(30)
    turtle.setheading(choice(direction))

screen = Screen()
screen.exitonclick()
 