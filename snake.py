from turtle import Turtle


class Snake:
    primal_positions = [(0, 0), (-20, 0), (-40, 0)]
    snake_parts = []

    for s in range(3):
        snake = Turtle()
        snake.color("white")
        snake.shape("square")
        snake.penup()
        snake.goto(primal_positions[s])
        snake_parts.append(snake)

    # for s in range(len(snake_parts)-1, 0, -1):
    #     new_x = snake_parts[s - 1].xcor()
    #     new_y = snake_parts[s - 1].ycor()
    #     snake_parts[s].goto(new_x, new_y)
    #     time.sleep(1)
    #     display.update()
    # for s in range(len(snake_parts)-1, 0, -1):
    #     new_x = snake_parts[s - 1].xcor()
    #     new_y = snake_parts[s - 1].ycor()
    #     snake_parts[s].goto(new_x, new_y)
    #     time.sleep(1)
    #     display.update()

    def move(self):

        for s in range(len(self.snake_parts) - 1, 0, -1):  # Moving 3rd piece to 2nd and 2nd piece to 1st
            new_x = self.snake_parts[s - 1].xcor()
            new_y = self.snake_parts[s - 1].ycor()
            self.snake_parts[s].goto(new_x, new_y)
        self.snake_parts[0].forward(20)

    def up(self):
        if self.snake_parts[0].heading() != 270:
            self.snake_parts[0].setheading(90)

    def down(self):
        if self.snake_parts[0].heading() != 90:
            self.snake_parts[0].setheading(270)

    def right(self):
        if self.snake_parts[0].heading() != 180:
            self.snake_parts[0].setheading(0)

    def left(self):
        if self.snake_parts[0].heading() != 0:
            self.snake_parts[0].setheading(180)

    def size_increase(self):
        last = (self.snake_parts[-1].xcor(), self.snake_parts[-1].ycor())
        snake = Turtle()
        snake.color("white")
        snake.shape("square")
        snake.penup()
        snake.goto(last)
        self.snake_parts.append(snake)
