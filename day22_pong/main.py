# Day 22: Pong capstone
import time
from turtle import Turtle, Screen
import paddle
from ball import Ball
# Paddle Class
#   user input function
# Ball Class
#   collision reflections
# Opponent Class (inherited by Paddle)
#   movement algorithm
# Scoreboard Class

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

my_paddle = paddle.Paddle()
my_paddle.goto(-350, 0)

opponent_paddle = paddle.Opponent()
opponent_paddle.goto(350, 0)


ball = Ball()

game_on = True
screen.listen()

while game_on:
    time.sleep(0.01)
    screen.update()
    if ball.ycor() > 295 or ball.ycor() < -295:
        ball.reflect_y()
    ball.detect_collision(my_paddle.xcor(), my_paddle.ycor())
    ball.detect_collision(opponent_paddle.xcor(), opponent_paddle.ycor())
    if ball.xcor() > 395 or ball.xcor() < -395:
        ball.refresh()
    opponent_paddle.track(ball.heading, ball.ycor)
    ball.move()
    screen.onkeypress(fun=my_paddle.move_up, key="w")
    screen.onkeypress(fun=my_paddle.move_down, key="s")



screen.exitonclick()
