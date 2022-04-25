from ctypes import alignment
from tkinter import font
from turtle import Screen, Turtle

FONT = ("Courier",60,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.player_1_score = 0
        self.player_2_score = 0
        
    def score(self,player):
        if player == 1:
            self.player_1_score += 1
        elif player == 2:
            self.player_2_score += 1
            
    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.player_1_score, align="center", font=FONT)
        self.goto(100,200)
        self.write(self.player_2_score,align="center",font=FONT)