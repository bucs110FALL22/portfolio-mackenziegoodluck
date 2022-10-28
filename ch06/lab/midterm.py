import turtle
import pygame

# screen
window = turtle.Screen()
window.bgcolor("Grey")
col = "purple"
# Creating the circle

def main(): 
  pen = turtle.Turtle()
  pen.color("black","orange")
  pen.begin_fill()
  pen.up()
  pen.goto(0,-100)
  pen.circle(100)
  pen.end_fill()
  pen.up()
  eye("red",5,pen)
  makeeyes(pen)
  nose(col,pen)
  makingmouth(pen)
  hat(pen)
  print (statement("Happy Halloween","Ha"))
def eye(color,radian, pen):
    '''
    general function description: meant to draw the eyes of the emoji, setting the 
    pen down and up, while setting the size of each circle
    args: It is a integer which is radian determining the size of each dot.
    return: none
    '''
    pen.down()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radian)
    pen.end_fill()
    pen.up()
def makeeyes(pen):
   '''
   general function:The function tells you the position of the eye,color, and the radius. Then,pen is added to make sure the 
    function can use the variable since it was introduced earlier.
   args: I used strings: to determine color and intergers when making the coordiante point of where to start drawing and 
   radian size of dot.
   return: none
   '''
   pen.goto(-50,50)
   eye("white",25,pen)
   pen.goto(-45,50)
   eye("purple",10,pen)
   pen.goto(50,50)
   eye("white",25,pen)
   pen.goto(45,50)
   eye("purple",10,pen)
#def nose
def nose(col,pen):
   '''
   general function: the function sets up the position for the nose and which direction it travels in. Since its a triangle, there are turns made to fit the face of the circle.
   args: (integer) the arguments consist ofnumber indiciting which direction the pen should move in to create a triangle
   return: none
   '''
   pen.up()
   pen.goto(-10,20)
   pen.down()
   pen.forward(35)
   pen.right(120) 
   pen.forward(35)
   pen.right(120)
   pen.forward(35)
   pen.right(120)
   pen.up()
def makingmouth(pen):#mouth
   '''
   general function description: The fucntion is creating placement for the mouth while using pen. I create  straight line,using this shape as the mouth of the emoji.
   args: (int: used for position of pen and movements taken to create the line, strings: used to determine color)
   return: none
   '''
   pen.goto(20,-50)
   pen.down()
   pen.right(180)
   pen.forward(50)
   pen.color("black")
   pen.up()
def hat(pen):
   '''
   general function description: The function creates a semi-circle cosplaying as a hat for the character drawn. The pen is taken to a point moved left, then the pen.circle gives us the radius.
   args: (ints: for the values of where shape is placed, srrings: color of shape)
   return: none
   '''
   pen.goto(40,100)
   pen.left(-40)
   pen.fillcolor("teal")
   pen.begin_fill()
   pen.circle(60,90)
   pen.end_fill()
   pen.hideturtle()
def statement(a,b):
   '''
   general function description: the function is  fulfilling the return vlaue aspect of the midterm. It sends a message to the 
 user at the end the drawing
   args: (string: used in statement aspect, int: used to multiply the statement three time)
   return: It returns the statement Happy Halloween, HaHaHa
   '''
   return a + b*3
main()



pygame.time.wait(1000)

  
