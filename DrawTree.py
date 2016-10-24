# Drawing a tree using the turtle tool
import turtle

def branch (t,angle,length,end_level):
	global level
	if level > end_level:
		return

	pos.append(t.pos())
	print len(pos)
	t.right(angle)
	t.forward(length)
	level = level + 1
	print level, end_level
	branch(t,angle,2*length/3,end_level)

	t.up() #Stop drawing
	t.goto(pos.pop()) #Go to prev intersection
	print len(pos)
	level = level - 1
	print level, end_level
	t.left(angle)
	t.down() #Start drawing
	t.forward(length)

	# if len(pos) < end_level:
	# 	branch(t,angle,length,end_level)



def draw():
	global pos
	global level
	pos = []
	loc = []
	level = 0
	window = turtle.Screen()
	window.bgcolor("white")

	t = turtle.Turtle()
	t.speed(1)
	t.color("#088A08")

	t.left(90)
	t.forward(100)
	branch(t,30,100,5)

	window.exitonclick()

draw()