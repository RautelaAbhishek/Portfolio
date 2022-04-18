from sys import setprofile
from turtle import Turtle,Screen
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

body_parts = []
game_on = True


for i in range(3):
    part = Turtle('square')
    part.color('white')
    part.penup()
    part.goto(x=(i-1)*-20,y=0)
    body_parts.append(part)

while game_on:
    screen.update()
    time.sleep(0.1)
    
    for part_num in range(len(body_parts) - 1, 0 , -1):
        new_xcor = body_parts[part_num - 1].xcor()
        new_ycor = body_parts[part_num - 1].ycor()
        body_parts[part_num].goto(new_xcor,new_ycor)
    
    body_parts[0].forward(20)
    
screen.listen()

screen.exitonclick()

