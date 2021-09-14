from turtle import Turtle
SCORE_POSITION = (0, 250)
ALIGNMENT = 'center'
FONT = ('Arial', 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(SCORE_POSITION)
        self.display_score()

    def display_score(self):
        self.write(f'SCORE: {self.points}   HIGH SCORE:{self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
            with open("data.txt", mode="w") as data:
                data.write(f'{self.points}')
        self.clear()
        self.points = 0
        self.display_score()

    def update_score(self):
        self.points += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)