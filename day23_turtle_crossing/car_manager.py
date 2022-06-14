from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_FIELD = 20


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(r.choice(COLORS))
        self.penup()
        x_pos = r.randint(300, 900)
        y_pos = r.randint(-200, 200)
        self.goto(x_pos, y_pos)


class CarManager:
    def __init__(self):
        self.step = STARTING_MOVE_DISTANCE
        self.car_list = []
        for i in range(CAR_FIELD):
            car = Car()
            self.car_list.append(car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(self.step)
            self.recycle(car)

    def recycle(self, car):
        if car.xcor() < -320:
            self.car_list.remove(car)
            new_car = Car()
            x_pos = r.randint(320, 400)
            y_pos = r.randint(-200, 200)
            new_car.goto(x_pos, y_pos)
            self.car_list.append(new_car)

    def level_up(self):
        self.step += MOVE_INCREMENT

    def detect_collision(self, turtle_gps):
        for car in self.car_list:
            if -30 < car.xcor() < 30:
                if -20 < (turtle_gps - car.ycor()) < 15:
                    return True
