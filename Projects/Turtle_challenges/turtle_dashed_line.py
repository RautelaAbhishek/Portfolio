from turtle import Screen,Turtle

turtle = Turtle()
for i in range(10):
    turtle.down()
    turtle.forward(10)
    turtle.up()
    turtle.forward(5)

screen = Screen()
screen.exitonclick()