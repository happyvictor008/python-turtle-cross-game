FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard:

    def __init__(self):
        self.score = 0

    def show_score(self):
        score = Turtle()
        score.clear()
        score.penup()
        score.hideturtle()
        score.setposition(-290,250)
        score.write(f"Score = {self.score}", align="left", font=FONT)


    def show_game_over(self):
        game_over = Turtle()
        game_over.clear()
        game_over.penup()
        game_over.setposition(-100,0)
        game_over.hideturtle()
        game_over.write(f"Game Over", align="left", font=FONT)