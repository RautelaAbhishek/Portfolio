from turtle import Turtle

class Bar(Turtle):
    def __init__(self,side):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.shape('square')
        self.resizemode('user')
        self.shapesize(1,5)
        self.seth(270)
        self.color('white')
        self.penup()
        self.goto(x=side,y=0)
        self.showturtle()
        self.heading()
        
    def down(self):
        if self.ycor() > -250:
            self.forward(10)
    
    def up(self):
        if 250 > self.ycor() :
            self.back(10)
    