from turtle import Screen, Turtle


turtle_a = Turtle()
turtle_a.shape('arrow')
turtle_a.color('red')
for i in range(4):
    turtle_a.forward(100)
    turtle_a.left(90)



screen = Screen()
screen.exitonclick()
