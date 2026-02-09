from turtle import Turtle

PADDLE_COLOR = "brown"
PADDLE_SIZE = 5
PADDLE_MOVE = 25

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=PADDLE_SIZE)
        self.penup()
        self.color(PADDLE_COLOR)
        self.goto(x_cor, y_cor)

    def go_up(self):
        if 250 > self.ycor():
            new_y = self.ycor() + PADDLE_MOVE
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - PADDLE_MOVE
            self.goto(self.xcor(), new_y)
