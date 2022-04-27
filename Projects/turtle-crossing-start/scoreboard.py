from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(x=-220,y=260)
        self.color('black')
        self.update()
        
    def update(self):
        self.clear()
        self.write(f"Level {self.level}",align='center',font=FONT)

    def add_score(self):
        self.level += 1
        self.update()
        
    def game_over(self):
        self = Turtle()
        self.hideturtle()
        self.penup()
        self.write('GAME OVER',align='center',font= FONT)