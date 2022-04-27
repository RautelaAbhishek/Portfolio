import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



# Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Player
player = Player()

# Scoreboard
score = Scoreboard()

# Screen Listen
screen.listen()
screen.onkeypress(player.move,'space')

# Cars
car_manager = CarManager()



# Main code
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_across()
    
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
    
    if player.at_finish_line():
        player.start()
        score.add_score()
        car_manager.level_up()
        

screen.exitonclick()