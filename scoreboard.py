from turtle import Turtle
SCORE_POSITION = (0, 250)
ALIGNMENT = 'center'
FONT = ('Arial', 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(SCORE_POSITION)
        self.display_score()

    def display_score(self):
        self.write(f'SCORE: {self.points}', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.points += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)