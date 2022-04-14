import random
from turtle import Screen,Turtle, color

turtle = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

sides = 3
turtle.forward(50)
while sides < 11:
    turtle.color(random.choice(colours))
    for i in range(sides):
        turtle.left(360/sides)
        turtle.forward(100)
    sides += 1
        
        






screen = Screen()
screen.exitonclick()