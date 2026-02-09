from turtle import Turtle

SCORE_COLOR = "cyan"
QUIT_COLOR = "gray"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(SCORE_COLOR)
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-50, 240)
        self.write(self.l_score, align="center", font=("Courier", 40, "bold"))
        self.goto(50, 240)
        self.write(self.r_score, align="center", font=("Courier", 40, "bold"))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

class Quit(Turtle):
    def __init__(self):
        super().__init__()
        self.color(QUIT_COLOR)
        self.shape("square")
        self.shapesize(stretch_wid=0.4,stretch_len=3)
        self.penup()
        self.goto(350, 270)
        self.write("QUIT", align="center", font=("Courier", 20, "bold"))