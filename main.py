from turtle import Screen
import time
from snake import Snake
from food import Food


screen = Screen()
screen.setup(width=600, height=600, startx=None, starty=None)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snek = Snake()
food = Food()

screen.listen()
screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")

game_on = True
while game_on:
  screen.update()
  time.sleep(0.1)
  snek.move()

  # Detect collision with wall
  if snek.head.xcor() > 285 or snek.head.xcor() < -285 or snek.head.ycor() > 285 or snek.head.ycor() < -285:
    snek.reset_snake()

screen.exitonclick()