# Day 18
import turtle
from turtle_moves import TurtleMoves
turtle.colormode(255)

tim = turtle.Turtle()
# tim.shape("turtle")
tim.color("blue")
# remember you can refactor variable names!
tim.speed("fastest")
tim.pensize(10)
tim.penup()
tim.setposition(-300, -300)
tim.pendown()
t_mobile = TurtleMoves(tim)
t_mobile.array_walk(30, 30)
# numboi = 50
# for i in range(numboi):
#     # t_mobile.rand_walk(20)
#     tim.circle(100)
#     tim.right(360 / numboi)
#     t_mobile.rand_color()







screen = turtle.Screen()
screen.exitonclick()
