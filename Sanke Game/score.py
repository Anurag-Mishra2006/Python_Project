from turtle import Turtle

ALIGNMENT="center"
FONT=("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.up()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle() # Read

    def update_scoreboard(self):
        self.write(f"Score:{self.score}",align=ALIGNMENT,font=FONT)


    def game_over(self):
        self.home()
        self.write("GAME OVER",align="center",font=FONT)

    def inc_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
