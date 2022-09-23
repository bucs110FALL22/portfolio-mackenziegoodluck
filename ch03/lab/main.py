import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
michelangelo.forward(random.randrange(1,101))
leonardo.forward(random.randrange(1,101))

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for i in range(11):
  michelangelo.forward(random.randrange(1,11))
  leonardo.forward(random.randrange(1,11))

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
#turtle quit
window.exitonclick()

# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode((640,600))

coords = []
num_sides = 3
side_length = 100
offset= 100

for i in range(num_sides):
  theta = (2.0 * math.pi * (i)/num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])


pygame.draw.polygon(window, "WHITE",coords)
  
pygame.display.flip()
pygame.time.wait(1000)
window.fill("Grey")

coords = []
num_sides = 4
side_length = 100
offset= 100

for i in range(num_sides):
  theta = (2.0 * math.pi * (i)/num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

pygame.draw.polygon(window,"PINK",coords)
  
pygame.display.flip()
pygame.time.wait(1000)
window.fill("Blue")

coords = []
num_sides = 6
side_length = 100
offset= 100

for i in range(num_sides):
  theta = (2.0 * math.pi * (i)/num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

pygame.draw.polygon(window,"PURPLE",coords)
  
pygame.display.flip()
pygame.time.wait(1000)
window.fill("Orange")

coords = []
num_sides = 9
side_length = 100
offset= 100

for i in range(num_sides):
  theta = (2.0 * math.pi * (i)/num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

pygame.draw.polygon(window,"RED",coords)
  
pygame.display.flip()
pygame.time.wait(1000)
window.fill("GREEN")


coords = []
num_sides = 360
side_length = 100
offset= 100

for i in range(num_sides):
  theta = (2.0 * math.pi * (i)/num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

pygame.draw.polygon(window,"Teal",coords)
  
pygame.display.flip()
pygame.time.wait(1000)
window.fill("Brown")





