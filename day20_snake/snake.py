import random as r
from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.speed = 10

    def create_snake(self):
        start_length = 3
        start_x = r.randint(-200, 200)
        start_y = r.randint(-200, 200)
        start_d = [0, 0, 0, 0]
        direc = r.randint(0, 3)
        start_d[direc] = 20
        for i in range(start_length):
            snake_segment = Turtle(shape="square")
            snake_segment.color("white")
            snake_segment.setheading(direc * 90)
            snake_segment.penup()
            snake_segment.goto(start_x - start_d[0] * i + start_d[2] * i,
                               start_y - start_d[1] * i + start_d[3] * i)
            self.snake_list.append(snake_segment)

    def move(self):
        for seg_num in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[seg_num - 1].xcor()
            new_y = self.snake_list[seg_num - 1].ycor()
            self.snake_list[seg_num].goto(new_x, new_y)
        self.snake_list[0].forward(self.speed)

    def left(self):
        self.snake_list[0].left(90)

    def right(self):
        self.snake_list[0].right(90)

    def lengthen(self):
        snake_segment = Turtle(shape="square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(self.snake_list[-1].xcor(), self.snake_list[-1].ycor())
        self.snake_list.append(snake_segment)
        self.speed += 1

    def refresh(self):
        for bebe in self.snake_list:
            bebe.goto(500, 500)  # clear the snake from the screen
        self.snake_list.clear()
        self.create_snake()
        self.speed = 10

    def ouch(self):
        # list slicing
        # list[2:5] of [0, 1, 2, 3, 4, 5, 6] is [2, 3, 4]!
        # list[:5] of [0, 1, 2, 3, 4] is [2, 3, 4]
        # list[2:5:2] of [0, 1, 2, 3, 4, 5, 6] is [2, 4]
        # list[::-1] of [0, 1, 2, 3, 4, 5, 6] is [6, 5, 4, ...]
        s = self.snake_list
        for i in range(1, len(s)):
            if s[i].xcor() - 5 < s[0].xcor() < s[i].xcor() + 5:
                if s[i].ycor() - 5 < s[0].ycor() < s[i].ycor() + 5:
                    return True
        return False

