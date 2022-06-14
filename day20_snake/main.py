import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

# NOTES
# !

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

game_on = True
screen.listen()
while game_on:

    snake.move()

    screen.onkeypress(key="a", fun=snake.left)
    screen.onkeypress(key="d", fun=snake.right)

    screen.update()

    # detect wall collision
    if snake.snake_list[0].xcor() > 285 or snake.snake_list[0].xcor() < -285 or snake.snake_list[0].ycor() > 285 or snake.snake_list[0].ycor() < -285:
        score.refresh()
        snake.refresh()
    # detect body collision
    if snake.ouch():
        score.refresh()
        snake.refresh()
    # detect collision w food
    if snake.snake_list[0].distance(food) < 15:
        # print("collision")
        food.refresh()
        snake.lengthen()
        score.point()

    time.sleep(0.05)

screen.exitonclick()
