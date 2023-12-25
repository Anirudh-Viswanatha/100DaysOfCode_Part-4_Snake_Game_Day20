from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.updatescore()

    def updatescore(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def point(self):
        self.score += 1
        self.clear()
        self.updatescore()

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)


