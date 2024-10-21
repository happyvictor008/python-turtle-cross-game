STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.move_distance = MOVE_DISTANCE
        self.starting_position = STARTING_POSITION
        self.reset_player()
        self.wining_rounds = 0

    def reset_player(self):
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(self.starting_position)

    def move_up(self):
        new_ycor = self.ycor() + MOVE_DISTANCE
        self.sety(new_ycor)

    def move_down(self):
        new_ycor = self.ycor() - MOVE_DISTANCE
        self.sety(new_ycor)

    def player_win(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.wining_rounds +=1
            return True
        else:
            return False