from turtle import Screen
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600, startx=None, starty=None)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

  # Detect collision with food
  if snake.head.distance(food) < 16:
    food.refresh()
    score.add_score()
    snake.extend()

  # Detect collision with wall
  if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
    snake.reset_snake()

  # Detect collision with snake's tail
  for segment in snake.snake[1:]:
    if snake.head.distance(segment) < 10:
      snake.reset_snake()
      food.refresh()

screen.exitonclick()