from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Snake()
food = Food()
score = Score()

screen.listen()
""" Movements """
screen.onkey(key='Up', fun=player.move_up)
screen.onkey(key='Down', fun=player.move_down)
screen.onkey(key='Left', fun=player.move_left)
screen.onkey(key='Right', fun=player.move_right)

game_is_on = True

while game_is_on:
    screen.update()
    player.animate_snake()
    player.snake_head.forward(20)
    time.sleep(0.08)

    # detect collision with food
    if player.snake_head.distance(food) < 15:
        food.respawn()
        player.extend_snake()
        player.snake_size += 1
        score.update_score()

    # detect collision with wall
    if player.snake_head.xcor() < -290 or player.snake_head.xcor() > 290 \
            or player.snake_head.ycor() < -290 or player.snake_head.ycor() > 290:

        game_is_on = False
        score.game_over()

    # detect collision with tail
    for node in player.snake_body[1:]:
        if player.snake_head.distance(node) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
