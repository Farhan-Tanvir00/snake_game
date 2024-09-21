from turtle import Turtle


class Score:
    with open("high_score.txt") as file:
        read_score = int(file.read())

    high_score = read_score
    total_score = 0

    score = Turtle()
    score.penup()
    score.goto(0, 280)
    score.color("white")
    score.hideturtle()

    def __init__(self):
        self.view_score()

    def view_score(self):
        self.score.clear()
        self.score.write(arg=f"SCORE : {self.total_score}   High Score = {self.high_score}",
                         align="center", font=('Arial', 10, 'normal'))

    def update_score(self):
        self.total_score += 1

    def game_over(self):
        self.update_highscore()
        self.score.goto(0, 0)
        self.score.color("red")
        self.score.pensize(3)
        self.score.write(arg="GAME OVER", align="center",  font=('Arial', 12, 'normal'))

    def update_highscore(self):
        if self.total_score > self.high_score:
            self.high_score = self.total_score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
            self.view_score()
