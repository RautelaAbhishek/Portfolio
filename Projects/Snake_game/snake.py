from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]
        
    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_part(pos)
            
    def add_part(self,pos):
        part = Turtle('square')
        part.color('white')
        part.penup()
        part.goto(pos)
        self.parts.append(part)
    
    def extend(self):
        self.add_part(self.parts[-1].position())
            
    def move(self):
        for part_num in range(len(self.parts) - 1, 0 , -1):
            new_xcor = self.parts[part_num - 1].xcor()
            new_ycor = self.parts[part_num - 1].ycor()
            self.parts[part_num].goto(new_xcor,new_ycor)
        self.head.forward(MOVE_DIST)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
            
    def reset(self):
        for part in self.parts:
            part.goto(1000,1000)
        self.parts.clear()
        self.create_snake()
        self.head = self.parts[0]
    