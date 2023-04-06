"""
Sarah Kudrick 4/3/2023
this generates the points of a binary tree and draws circles at each point.
Each circle's radius is adjusted so that
#the 4 grandchildren points of that point all lie on the edge of that circle.
It prints the list of points as well as the orientation in degrees. 
It also plots the points in python turtle.
"""

import turtle
import math

t = turtle.Turtle()
t.penup()
t.speed(0)
colors = [0.74, 0.49, 0.74]
t.color(colors[0], colors[1], colors[2])
#change rounds to adjust the "height" of the binary tree
#in other words how many nodes on a path from root to leaf
#in other words how many layers of branches
rounds = 10
print("Number of rounds: " + str(rounds))
#change scale to adjust how big or small the binary tree will be in pixels.
#60 is a value for scale that fits well in the replit window.
scale = 60.0
print("Scale: " + str(scale))
length = (float)(scale * 2.0 / math.sqrt(2))
print("Initial length: " + str(length))
mult = (float)(math.sqrt(2) / 2)
print("Mulitplier: " + str(mult))
radius = (float)(scale * math.sqrt(5))
print("Radius: " + str(radius))
#list will be rewritten repeatedly in the loop.
list = [[0.0, -length, 0]]
#biglist will store all of the node coordinates and orientations
#for all layers of the tree, root to leaves.
biglist = [list]
#these next lines create the circle at the root of the tree.
t.goto(list[0][0], list[0][1])
t.dot()
t.goto(0, (float)(60.0 * (-math.sqrt(5) - math.sqrt(2))))
t.pendown()
t.begin_fill()
t.circle(radius)
t.end_fill()
t.penup()

for round in range(rounds):
  newlist = []
  radius = radius / math.sqrt(2)
  #this for loop creates a color adjustment at the beginning of each layer.
  for i in range(3):
    colors[i] = (colors[i] + .025 * (i + 1)) % 1.0
  t.color(colors[0], colors[1], colors[2])

  #this for loop adds all nodes to the running list for this round, or layer
  #and then draws each of these nodes.
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
  print("Iteration " + str(round) + ": " + str(len(newlist)) + " points")
  print(newlist)
  for point in newlist:
    t.goto(point[0], point[1])
    t.dot()
    t.goto(point[0], point[1] - radius)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()

  #before moving onto the next layer,
  #all of the nodes of this layer are copied into the biglist.
  list = newlist.copy()
  biglist.append(newlist)
  length = length * mult
