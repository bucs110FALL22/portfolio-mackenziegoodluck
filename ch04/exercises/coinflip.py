import turtle
import random

window = turtle.Screen()
window.bgcolor('pink')

Turtle = turtle.Turtle()

turtle.goto(100,100)
distance = 10
angle = 90
is_in_screen = True

colors = ["green", "blue", "purple"]

while is_in_screen:
  coin = random.randge(0,2)
if coin:
  t.right(angle)

else:
  t.left(angle)
  t.forward(distance)


 turtkeX = t.xcor()
 turtleY = t.ycor()

 x_range = wn.window_width()/2
 y_range = wn.window_height()/2
if abs(turtleX) > x_range or abs(turtleY) > y_range
 is_in_screen = False

wn.bgcolor ("Yellow")
wn.exitonclick()
