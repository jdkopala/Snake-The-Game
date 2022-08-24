from turtle import Screen
import time
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600, startx=None, starty=None)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snek = Snake()


screen.listen()

game_on = True
while game_on:
  screen.update()
  time.sleep(0.1)
  snek.move()

screen.exitonclick()