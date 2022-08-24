from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open ('highscore.txt') as data:
            self.high_score = int(data.read())
        self.speed('fastest')
        self.ht()
        self.pu()
        self.color('white')
        self.draw_scoreboard()
    
    def draw_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.draw_scoreboard()