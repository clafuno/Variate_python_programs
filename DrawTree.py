# Drawing a tree using the turtle tool
import turtle

def branch (t,angle,length,level,end_level):
	if level > end_level:
		return

	alpha = angle
	pos.append(t.pos())
	#print len(pos)
	t.right(angle)
	t.forward(length)
	level = level + 1
	#print level, end_level

	branch(t,angle,2*length/3,level,end_level) #Right branches

	t.up() #Stop drawing
	t.goto(pos.pop()) #Go to prev intersection
	#print len(pos)
	#level = level - 1
	#print level, end_level
	t.left(angle)
	t.down() #Start drawing
	t.forward(length)

	branch(t,-angle,2*length/3,level,end_level) #Left branches


def draw():
	global pos
	pos = []
	level = 0
	window = turtle.Screen()
	window.bgcolor("white")

	t = turtle.Turtle()
	t.speed(10)
	t.color("#088A08")
	t.goto(0,-100)

	t.left(90)
	t.forward(100)
	branch(t,30,100,level,5)

	window.exitonclick()

draw()