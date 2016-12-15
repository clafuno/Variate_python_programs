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

	branch(t,angle,3*length/4,level,end_level) #Right branches

	t.up() #Stop drawing
	t.goto(pos.pop()) #Go to prev intersection
	#print len(pos)
	#level = level - 1
	#print level, end_level
	t.left(angle)
	t.down() #Start drawing
	t.forward(length)

	branch(t,-(angle+20),3*length/4,level,end_level) #Left branches

	#NOTE: t.heading()

def draw():
	global pos
	pos = []
	angle = 35
	length = 100
	level = 0
	end_level = 6
	window = turtle.Screen()
	window.bgcolor("white")

	t = turtle.Turtle()
	t.speed(10)
	t.color("#088A08")
	t.goto(0,-100)

	t.left(90)
	t.forward(100)
	branch(t,angle,length,level,end_level)

	window.exitonclick()

draw()