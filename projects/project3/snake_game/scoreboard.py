from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# Always use the SAME data.txt file in the SAME folder as this script
FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        # --- Load high score safely ---
        try:
            with open(FILE_PATH, "r") as data:
                content = data.read().strip()
                self.high_score = int(content) if content else 0
        except FileNotFoundError:
            self.high_score = 0

        # --- Draw scoreboard ---
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}",
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_scoreboard()

    def reset(self):
        # Save high score to data.txt
        with open(FILE_PATH, "w") as data:
            data.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()
