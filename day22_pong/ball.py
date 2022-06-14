import time
import turtle
import random as r


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.refresh()
        self.zoom = 5
        self.speed("fastest")

    def move(self):
        self.forward(self.zoom)

    def refresh(self):
        self.goto(0, 0)
        self.setheading(r.choice([-165, -150, -135, -45, -30, -15, 15, 30, 45, 135, 150, 165]))
        self.zoom = 5
        for i in range(3):
            self.hideturtle()
            time.sleep(0.25)
            self.showturtle()
            time.sleep(0.25)

    def detect_collision(self, paddle_x, paddle_y):
        if self.xcor() < -340 or self.xcor() > 340:
            if (paddle_y - 50) < self.ycor() < (paddle_y + 50):
                self.reflect_x()
                self.zoom += 1

    def reflect_y(self):
        current_heading = self.heading()
        self.setheading(current_heading * (-1))

    def reflect_x(self):
        current_heading = self.heading()
        if current_heading > 180:
            self.setheading((current_heading - 90) * (-1) + 90)
        else:
            self.setheading((current_heading + 90) * (-1) - 90)



