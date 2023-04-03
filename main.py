"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle
import math

t = turtle.Turtle()
t.penup()
t.speed(0)
t.color('pink')
colors = ['yellow', 'orange', 'pink']
colorint = 0
t.color(colors[colorint])
length = (float)(2 * 65 / math.sqrt(2))
print(length)
mult = (float)(math.sqrt(2) / 2)
print(mult)
list = [[0.0, -length, 0]]
t.goto(list[0][0], list[0][1])
t.dot()
for round in range(11):
  newlist = []
  for item in list:
    newlist.append([
      item[0] + (length * math.sin(math.radians((item[2] - 45) % 360))),
      item[1] + (length * math.cos(math.radians((item[2] - 45) % 360))),
      (item[2] - 45) % 360
    ])
    newlist.append([
      item[0] + (length * math.sin(math.radians((item[2] + 45) % 360))),
      item[1] + (length * math.cos(math.radians((item[2] + 45) % 360))),
      (item[2] + 45) % 360
    ])
  print(newlist)
  colorint = (colorint + 1) % 3
  t.color(colors[colorint])
  for point in newlist:
    t.goto(point[0], point[1])
    t.dot()
  list = newlist.copy()
  length = length * mult
