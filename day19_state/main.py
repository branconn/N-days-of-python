# Day 19: States, Instances, and Event Logging
from turtle import Turtle, Screen
import random
# NOTES & CHALLENGES
# turtle has event listeners turtle.listen()
# state is the setting of an object instance
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

screen = Screen()
screen.setup(width=500, height=400)
turtle_list = []
for i in range(len(colors)):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[i])
    t.goto(-230, (-90+i*30))
    turtle_list.append(t)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? (ROYGBIV)")

if user_bet:
    race_on = True

while race_on:
    for turtle in turtle_list:
        r_dist = random.randint(5, 20)
        r_angle = 20 * (random.random() - 0.5)
        turtle.forward(r_dist)
        turtle.setheading(r_angle)
        x_position = turtle.pos()[0]
        if x_position >= 230 and race_on:
            race_on = False
            winner = colors[turtle_list.index(turtle)]
if user_bet.lower() == winner:
    screen.title(f"The winner is {winner}!!   You win your bet!!!")
else:
    screen.title(f"The winner is {winner}!!   You lose your bet :/")



# def move_forwards():
#     t.forward(5)
#
#
# def move_backwards():
#     t.backward(5)
#
#
# def rotate_ccw():
#     t.left(5)
#
#
# def rotate_cw():
#     t.right(5)
#
#
# def shake():
#     t.clear()
#     t.reset()


# screen.listen()
# screen.onkeypress(key="w", fun=move_forwards)
# screen.onkeypress(key="a", fun=rotate_ccw)
# screen.onkeypress(key="s", fun=move_backwards)
# screen.onkeypress(key="d", fun=rotate_cw)
# screen.onkeypress(key="c", fun=shake)
# when you pass a function as an input, you exclude the ()!
screen.exitonclick()
# this concept is known as a higher order function (function using function)
# good for listening for events and executing something
# good practice to use keyword arguments for these

