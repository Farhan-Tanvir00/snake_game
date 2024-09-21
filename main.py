from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score
from walls import Walls

game_on = True

display = Screen()
display.setup(width=600, height=600)
display.bgcolor("black")
display.title("Snake Master")
display.tracer(0)

food = Food()
snake = Snake()
score = Score()
walls = Walls()

display.listen()
display.onkey(snake.up, "Up")
display.onkey(snake.down, "Down")
display.onkey(snake.left, "Left")
display.onkey(snake.right, "Right")

while game_on:
    display.update()
    time.sleep(0.1)
    snake.move()

    got_food = snake.snake_parts[0].distance(food)  # snake_part[0] is the snake head...
    if got_food < 14:
        score.update_score()
        score.view_score()
        snake.size_increase()
        food.gen_new()

    if (snake.snake_parts[0].xcor() > 270 or snake.snake_parts[0].xcor() < -270 or
            snake.snake_parts[0].ycor() > 270 or snake.snake_parts[0].ycor() < -270):
        score.game_over()
        game_on = False

    face = snake.snake_parts[0]
    for part in snake.snake_parts:
        if part == face:
            pass
        elif face.distance(part) < 10:
            game_on = False
            score.game_over()


display.exitonclick()
