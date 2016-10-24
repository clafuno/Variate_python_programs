# Drawing a tree using the turtle tool
import turtle

def branch (t,angle,length):
	init = t.pos()
	t.right(angle)
	t.forward(length)
	t.goto(init)
	t.left(2*angle)
	t.forward(length)

def draw():
	window = turtle.Screen()
	window.bgcolor("white")

	t = turtle.Turtle()
	t.speed(1)
	t.color("#088A08")

	t.left(90)
	t.forward(100)
	branch(t,30,40)


	window.exitonclick()

draw()