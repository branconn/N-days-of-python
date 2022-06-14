import random
from color_field import listed_colors

class TurtleMoves:
    def __init__(self, tim):
        self.turtle = tim
        self.palette = listed_colors

    def draw_shape(self, sides):
        angle = 360 / sides
        for i in range(sides):
            self.turtle.forward(100)
            if sides % 2 == 0:
                self.turtle.left(angle)
            else:
                self.turtle.right(angle)

    def rand_color(self):
        r = random.random()
        b = random.random()
        g = random.random()
        self.turtle.pencolor(r, b, g)
        # a tuple is an ordered immutable list (simplistic def)

    def choice_color(self):
        color = random.choice(self.palette)
        self.turtle.pencolor(color)

    def rand_walk(self, length):
        angle = random.choice([0, 90, 180, 270])
        self.turtle.left(angle)
        self.turtle.forward(length)

    def array_walk(self, r, c):
        for j in range(r):
            for i in range(c):
                self.turtle.forward(1)
                self.turtle.penup()
                self.turtle.forward(20)
                self.turtle.pendown()
                self.choice_color()
            if j % 2 == 0:
                self.turtle.forward(1)
                self.turtle.penup()
                self.choice_color()
                self.turtle.left(90)
                self.turtle.forward(20)
                self.turtle.left(90)
                self.turtle.pendown()
            else:
                self.turtle.forward(1)
                self.turtle.penup()
                self.choice_color()
                self.turtle.right(90)
                self.turtle.forward(20)
                self.turtle.right(90)
                self.turtle.pendown()




