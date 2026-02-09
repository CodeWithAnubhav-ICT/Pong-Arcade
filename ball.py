from turtle import Turtle

BALL_SPEED_INCREASE = 0.80
BALL_SPEED = 0.05
BALL_COLOR = "yellow"
BALL_SHAPE = "circle"
BALL_MOVE = 5

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.penup()
        self.color(BALL_COLOR)
        self.ball_speed = BALL_SPEED
        self.x_move = BALL_MOVE
        self.y_move = BALL_MOVE

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.ball_speed *= BALL_SPEED_INCREASE

    def reset_position(self):
        self.goto(0,0)
        self.paddle_bounce()