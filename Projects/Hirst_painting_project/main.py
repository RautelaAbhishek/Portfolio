import colorgram
from turtle import Turtle,Screen,colormode
from random import choice

colors = colorgram.extract('Hirst_painting_project\painting.jpg', 30)
rgb_colors = [(28, 107, 163), (230, 160, 60), (190, 40, 81), (232, 214, 90), (219, 137, 174), (141, 106, 58), (108, 192, 215), (21, 56, 131), (204, 166, 31), (211, 72, 94), (234, 89, 57), (140, 29, 70), (119, 191, 144), (142, 208, 227), (9, 183, 169), (107, 107, 194), (11, 155, 87), (97, 50, 36), (23, 160, 205), (230, 167, 185), (84, 45, 33), (31, 43, 85), (32, 84, 89), (173, 185, 222), (237, 173, 160), (151, 214, 192)]


#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,b)
#    rgb_colors.append(new_color)


turtle = Turtle()
colormode(255)
turtle.speed(0)
turtle.up()
turtle.hideturtle()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
number_of_dots = 100

for i in range(1,number_of_dots + 1):

    turtle.dot(20,choice(rgb_colors))
    turtle.forward(50)
    if i % 10 == 0:
        
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)
    


screen = Screen()
screen.exitonclick()