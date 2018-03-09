#!/bin/python3

# This code is based on Code Club's: https://codeclubprojects.org/en-GB/python/turtle-race/
from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

# Setting up the lanes for the race!
for step in range(15):
  write(step, align='center')
  right(90)
  for num in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(20)

# Create the Ada turtle
ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

for turn in range(10):
  ada.right(36)

# Create the Bob turtle
bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

for turn in range(72):
  bob.left(5)

# Create the Ivy turtle
ivy = Turtle()
ivy.shape('turtle')
ivy.color('green')

ivy.penup()
ivy.goto(-160, 40)
ivy.pendown()

for turn in range(60):
  ivy.right(6)

# You should create your own turtle here!
  
# Here were start the race but moving each turtle a 
# random distance forward
for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  ivy.forward(randint(1,5))
  # Remember to add your turtle to the race too!
