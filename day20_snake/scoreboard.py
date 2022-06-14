from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.num_score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def point(self):
        self.num_score += 1
        self.clear()
        self.update_scoreboard()
        # print(self.num_score)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.num_score} | High Score: {self.high_score}", align="center", font=("Arial", 12, "normal"))

    def refresh(self):
        if self.num_score > self.high_score:
            self.high_score = self.num_score
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")
        self.num_score = 0
        self.update_scoreboard()

    # def over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER\nFinal Score: {self.num_score}", align="center", font=("Arial", 24, "normal"))
