from turtle import Turtle
import random


# ................slower....................

# class Food:
#     food = Turtle()
#     food.color("green")
#     food.penup()
#     food.shapesize(0.5, 0.5)
#     x = random.randint(-280, 280)
#     y = random.randint(-280, 280)
#     food.goto(x, y)
#     food.shape("circle")
#     food.speed("fastest")

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shapesize(0.7, 0.7)
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        # x = random.randint(-280, 280)
        # y = random.randint(-280, 280)
        # self.goto(x, y)
        self.gen_new()

    def gen_new(self):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        self.goto(x, y)
