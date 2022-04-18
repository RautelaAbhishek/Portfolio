STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]

class Snake:
    
    def __init__(self,name):
        self.part = []
        self.create_snake()
        
    def create_snake(self):
        for i in range(3):
            part = Turtle('square')
            part.color('white')
            part.penup()
            part.goto(x=(i-1)*-20,y=0)
            body_parts.append(part)