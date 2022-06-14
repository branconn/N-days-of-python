import turtle
import random as r


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_coord = r.randint(-280, 280)
        y_coord = r.randint(-280, 280)
        self.goto(x_coord, y_coord)
        self.rand_color()

    def rand_color(self):
        red = r.random()
        b = r.random()
        g = r.random()
        self.color(red, b, g)
