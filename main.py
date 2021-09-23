import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
def race():
  distance = random.randrange(1,100)
  leonardo.forward(distance)
  michelangelo.forward(distance)
  
race() 
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

from time import sleep
window.tracer(0)

while True:
    sleep(0.1)
    michelangelo.forward(random.randrange(0,10))
    leonardo.forward(random.randrange(0, 10))
    window.update()

race()

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here


window.exitonclick()
