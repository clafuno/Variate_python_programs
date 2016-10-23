# Udacity course - PROGRAMMING FOUNDATIONS WITH PYTHON
# Programm 3: Drawing Turtle in Python

import turtle

def draw_square(chosenturtle):
	for i in range(0,4):
		chosenturtle.forward(100)
		chosenturtle.right(90)

def draw():
#Create the window
	window = turtle.Screen()
	window.bgcolor("white")
#Create & customize turtle
	tur = turtle.Turtle()
	tur.color("blue")
	tur.speed(2)
	draw_square(tur)
	window.exitonclick()

draw()

