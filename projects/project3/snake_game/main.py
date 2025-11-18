from turtle import Screen, Turtle
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

# ----- Screen Setup -----
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# ----- Game Objects -----
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# ----- Controls -----
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# ----- Button Functions -----
def restart_game(_x, _y):
    """restart the game."""
    scoreboard.reset()
    snake.reset()
    game_loop()

def exit_game(_x, _y):
    """Close the game."""
    screen.bye()

# ----- Game Over -----
def game_over():
    """Display Game Over and update scoreboard."""
    scoreboard.reset()  # <-- this will save high score to data.txt
    # Show Game Over message in middle
    game_over_text = Turtle()
    game_over_text.hideturtle()
    game_over_text.color("red")
    game_over_text.penup()
    game_over_text.goto(0, 0)
    game_over_text.write("GAME OVER", align="center", font=("Arial", 30, "bold"))


# ----- Main Game Loop -----
def game_loop():
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or
            snake.head.ycor() > 260 or snake.head.ycor() < -290):
            game_is_on = False
            game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                game_over()

# ---- START GAME ----
game_loop()
screen.mainloop()