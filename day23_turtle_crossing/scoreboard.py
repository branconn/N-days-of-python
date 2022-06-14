from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.goto(-280, 260)
        self.level_up()

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, align="left", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write("GAME OVER", False, align="center", font=FONT)
