from ast import Break
from hashlib import new
from turtle import Pen, Screen, Turtle, color, speed
import random




screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which Turtle will win the race? Enter a colour:')

y_positions = [100,60,20,-20,-60,-100]
colours = ['red', 'green', 'blue', 'orange', 'purple', 'black']
turtle_list = []
ongoing_race = True

for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.speed(0)
    new_turtle.color(colours[i])
    new_turtle.goto(x=-230,y=y_positions[i])
    turtle_list.append(new_turtle)

while ongoing_race:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            ongoing_race = False
            if winning_color == user_bet:
                print(f'You\'ve won! The {winning_color} turtle won.')
            else:
                print(f'You\'ve lost! The {winning_color} turtle won.')
            Break
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
    
print(turtle_list)
screen.exitonclick()