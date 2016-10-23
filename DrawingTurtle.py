# Udacity course - PROGRAMMING FOUNDATIONS WITH PYTHON
# Programm 3: Drawing Turtle in Python

import turtle

def draw_square():
#Create the window
	window = turtle.Screen()
	window.bgcolor("white")

#Grab the turtle and indicate the movement to draw a square
	tur = turtle.Turtle()
	for i in range(0,4):
		tur.forward(100)
		tur.right(90)

	window.exitonclick()

draw_square()

