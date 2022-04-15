from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def angle_right():
    new_angle = tim.heading() - 5
    tim.setheading(new_angle)

def angle_left():
    new_angle = tim.heading() + 5
    tim.setheading(new_angle)
    
def clear_screen():
    tim.reset()

screen.listen()

screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='d', fun=angle_right)
screen.onkey(key='a', fun=angle_left)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()