from turtle import Turtle
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

  def __init__(self):
    self.snek = []
    self.create_snake()
    self.head = self.snek[0]

  def create_snake(self):
    for position in STARTING_POS:
      self.add_segment(position)

  def add_segment(self, position):
    segment = Turtle("square")
    segment.color("white")
    segment.pu()
    segment.goto(position)
    self.snek.append(segment)

  def move(self):
    for seg_num in range(len(self.snek) - 1, 0, -1):
      new_x = self.snek[seg_num - 1].xcor()
      new_y = self.snek[seg_num - 1].ycor()
      self.snek[seg_num].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)