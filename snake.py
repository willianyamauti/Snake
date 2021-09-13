from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_size = 3
        self.snake_color = 'green'
        self.last_node_position = [0, 0]
        self.snake_body = []
        self.create_snake_body()
        self.snake_head = self.snake_body[0]

    def create_snake_body(self):
        for n in range(self.snake_size):
            self.create_snake_node(self.last_node_position)

    def create_snake_node(self, position):
        snake = Turtle(shape='square')
        snake.color(self.snake_color)
        snake.penup()
        snake.goto(position)
        self.last_node_position = (snake.xcor() - 20, snake.ycor())
        self.snake_body.append(snake)

    def extend_snake(self):
        self.create_snake_node(self.snake_body[-1].position())

    def animate_snake(self):
        for segment in range(self.snake_size - 1, 0, -1):
            x = self.snake_body[segment - 1].xcor()
            y = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(x, y)

    def move_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def move_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def move_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def move_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
