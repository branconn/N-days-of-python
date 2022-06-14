from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5)
        self.setheading(90)
        self.color("white")
        self.speed("fastest")

    def move_up(self):
        if self.ycor() < 250:
            self.forward(15)

    def move_down(self):
        if self.ycor() > -250:
            self.backward(15)


class Opponent(Paddle):
    def __init__(self):
        super().__init__()

    def track(self, ball_heading, ball_ycor):
        if ball_heading() < 90 or ball_heading() > 270:
            if ball_ycor() - self.ycor() > 15:
                self.move_up()
            elif ball_ycor() - self.ycor() < -15:
                self.move_down()







