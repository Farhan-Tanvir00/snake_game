from turtle import Turtle


class Walls(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.draw_square()

    def draw_square(self):
        self.penup()
        self.goto(-275, 275)
        self.pensize(5)
        self.pendown()
        self.forward(550)
        self.setheading(270)
        self.forward(550)
        self.setheading(180)
        self.forward(550)
        self.setheading(90)
        self.forward(550)
        self.hideturtle()

