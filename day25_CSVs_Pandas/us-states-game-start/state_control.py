from turtle import Turtle


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def label(self, text, coordinates):
        self.penup()
        self.goto(coordinates)
        self.pendown()
        self.write(text, align="center")
