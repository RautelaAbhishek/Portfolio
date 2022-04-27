from turtle import Turtle

ALIGNMENT ='center'
FONT = ('arial',24,'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        
        with open("Snake_game\data.py") as data:
            self.high_score = int(data.read())
        
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0,260)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align=ALIGNMENT,font=FONT)
    
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
      
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Snake_game\data.py", mode='w') as data:
                data.write(str(self.score))
        self.score = 0
        self.update_scoreboard()
        
    
    def game_over(self):
        self.goto(0,0)
        # self.write(f"GAME OVER",align=ALIGNMENT,font=FONT)
        
    def get_high_score(self):
        with open("Snake_game\data.py") as self.file:
            new_high_score = self.file.read
            
            
    # def store_high_score(self):
    #     with open("Snake_game\data.py", mode='w') as self.file:
    #         self.file.write(self.high_score)
            
    
        