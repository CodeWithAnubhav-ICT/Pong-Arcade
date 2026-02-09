from turtle import Screen
from ball import Ball, BALL_SPEED
from paddle import Paddle, PADDLE_SIZE
from scoreboard import Scoreboard, Quit
import time

# SCREEN
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.bgpic(picname="bg2.gif")
screen.title("Pong")
screen.tracer(0)

# OBJECTS
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()
off = Quit()

# EXIT FUNCTION
def game_off(x,y):
    global game_is_on
    game_is_on = False
    return game_is_on

# KEYS AND BUTTONS
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_down, "s")
off.onclick(game_off)

#MAIN
game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.wall_bounce()

    if ball.distance(r_paddle) < 10*PADDLE_SIZE and ball.xcor() > 320 or ball.distance(l_paddle) < 10*PADDLE_SIZE and ball.xcor() < -320 :
        ball.paddle_bounce()

    if ball.xcor() > 380 :
        time.sleep(1)
        ball.ball_speed = BALL_SPEED
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380 :
        time.sleep(1)
        ball.ball_speed = BALL_SPEED
        ball.reset_position()
        scoreboard.r_point()

    screen.update()
