from turtle import Turtle

# Constants
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

  def __init__(self):
    self.snake = []
    self.create_snake()
    self.head = self.snake[0]

  def create_snake(self):
    for position in STARTING_POS:
      self.add_segment(position)

  def reset_snake(self):
    for seg in self.snake:
      seg.goto(1000, 1000)
    self.snake.clear()
    self.create_snake()
    self.head = self.snake[0]

  def add_segment(self, position):
    segment = Turtle("square")
    segment.color("white")
    segment.pu()
    segment.goto(position)
    self.snake.append(segment)

  def move(self):
    for seg_num in range(len(self.snake) - 1, 0, -1):
      new_x = self.snake[seg_num - 1].xcor()
      new_y = self.snake[seg_num - 1].ycor()
      self.snake[seg_num].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)

  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)
  
  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)