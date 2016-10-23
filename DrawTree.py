# Drawing a tree using the turtle tool
import turtle

def brach(turtle,angle,length,scale):
	t.forward(length)
	t.right(angle)
	# Insert blanch here (https://discussions.udacity.com/uploads/default/12490/c605ef44e8ec28fc.png)
	t.forward(length/2)
	t.left(180)
	t.forward(length/2)
	t.left(angle+180+angle)
	t.forward(length)

def draw():
	window = turtle.Screen()
	window.bgcolor("white")

	t = turtle.init()
	t.speed(10)

	t.left(90)
	t.color("green")




	window.exitonclick()
