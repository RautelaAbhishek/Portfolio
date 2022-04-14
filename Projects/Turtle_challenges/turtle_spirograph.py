from turtle import Screen,Turtle,colormode
from random import randrange


turtle = Turtle()
turtle.speed(0)
colormode(255)
direction = 0

def rand_colour():
    r = randrange(0,255)
    g = randrange(0,255)
    b = randrange(0,255)
    color = (r,g,b)
    return color

for i in range(60):
    turtle.color(rand_colour())
    turtle.setheading(direction)
    turtle.circle(100)
    direction += 6

    


screen = Screen()
screen.exitonclick()