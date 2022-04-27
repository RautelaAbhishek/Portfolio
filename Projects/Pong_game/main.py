from random import Random
from turtle import Screen,Turtle
from bar import Bar
from ball import Ball
from scoreboard import Scoreboard
import time

# Constants
LINE = 20
GAP = 20
GAME_ON = True

sleep_amt = 0.1

# Initialize Screen
screen = Screen()
# Screen Initial Setup
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
    
# Initialize Bars
player_1 = Bar(-350)
player_2 = Bar(350)    

# Initialize Ball
ball = Ball()

# Initialize Scoreboard
scoreboard = Scoreboard()
scoreboard.update()


# Listen Events
screen.listen()
screen.onkeypress(player_2.up,"Up")
screen.onkeypress(player_1.up,"w")
screen.onkeypress(player_2.down,"Down")
screen.onkeypress(player_1.down,"s")

# Loop while game is running
while GAME_ON:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect collision with bar
    if ball.distance(player_2) < 60 and 350 > ball.xcor() > 330 or ball.distance(player_1) < 60 and -350 < ball.xcor() < -330 :
        ball.bounce_x()

    # Detect out of bounds
    if ball.xcor() > 385:
        ball.reset()
        ball.x_move *= -1
        scoreboard.score(2)
        scoreboard.update()
    
    if ball.xcor() < -385:
        ball.reset()
        ball.x_move *= -1  
        scoreboard.score(1)
        scoreboard.update()
        
    sleep_amt *= 0.99
          
# Exit on Click
screen.exitonclick()
