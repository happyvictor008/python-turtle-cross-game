import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.listen()

wining_round = 0
carmanager = CarManager()


scoreboard = Scoreboard()

car_generate_loop = 6
car_generate = 0
car_list = []
game_is_on = True

while game_is_on:
    scoreboard.score = wining_round
    scoreboard.show_score()
    print(len(carmanager.car_list))
    time.sleep(0.1)
    screen.update()
    car_generate += 1


    if player.player_win():
        #carmanager.car_list = []
        wining_round += 1
        #screen.resetscreen()
        player.reset_player()
        carmanager.speed_up(wining_round)


    if car_generate > 6:
        carmanager.generate_car()
        car_generate = 0
    carmanager.car_move()


    for car in carmanager.car_list:
        if car.distance(player) <= 20:
            game_is_on = False
            scoreboard.show_game_over()
            screen.title("GAME OVER")






screen.exitonclick()