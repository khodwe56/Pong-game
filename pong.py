### A simple pong game.

import turtle
import os


## Creating a window and defining it
window = turtle.Screen()
window.title("pong game")
window.bgcolor("black")

#Dimmensionality starts from center of screen.
window.setup(width = 800,  height=600)
##Everything has to be updated manually
window.tracer(0)


###Paddle 1

##Object of class Turtle
pa = turtle.Turtle()
## Speed to 0 as special meaning it turns off the animation and goes as fast as possinble.

pa.speed(0)
pa.shape("square")
pa.color("red")

##To stretch the paddle to required sixe use this.

pa.shapesize(stretch_wid = 5, stretch_len = 1)
##penup ensures that the object leaves no ink on the screen and pendown does the exact opposite.
pa.penup()

## Begins from co-ordinate (-350,0) the second and third quandrant axis line.
pa.goto(-350,0)


###Paddle 1

##Object of class Turtle
pb = turtle.Turtle()
## Speed to 0 as special meaning it turns off the animation and goes as fast as possinble.

pb.speed(0)
pb.shape("square")
pb.color("red")

##To stretch the paddle to required sixe use this.

pb.shapesize(stretch_wid = 5, stretch_len = 1)
##penup ensures that the object leaves no ink on the screen and pendown does the exact opposite.
pb.penup()

## Begins from co-ordinate (-350,0) the second and third quandrant axis line.
pb.goto(350,0)

###Paddle 1

##Object of class Turtle
ball = turtle.Turtle()
## Speed to 0 as special meaning it turns off the animation and goes as fast as possinble.

ball.speed(0)
ball.shape("circle")
ball.color("blue")

##To stretch the paddle to required sixe use this.

#pa.shapesize(stretch_wid = 5, stretch_len = 1)
##penup ensures that the object leaves no ink on the screen and pendown does the exact opposite.
ball.penup()

## Begins from co-ordinate (-350,0) the second and third quandrant axis line.
ball.goto(0,0)

## Moving the ball by movinfg it with specific frames.

ball.dx = 0.12
ball.dy = -0.12

### Creatng a scorecard for the players using pen functionality of the turtle.

pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,240)
pen.write("Player 1 : 0 \nPlayer 2 : 0",align = 'center',font = ("Courier",20,"normal"))



def pa_up():
	y = pa.ycor()
	y+=20
	pa.sety(y)

def pa_down():
	y = pa.ycor()
	y-=20
	pa.sety(y)

def pb_up():
	y = pb.ycor()
	y+=20
	pb.sety(y)

def pb_down():
	y = pb.ycor()
	y-=20
	pb.sety(y)			

#Making our prpgram listen to keyboard bindings.
window.listen()
window.onkeypress(pa_up,"w")
window.onkeypress(pa_down,"s")
window.onkeypress(pb_up,"Up")
window.onkeypress(pb_down,"Down")

##Main game loop.

sa = 0
sb = 0
while True:
	window.update()

	###Sctually moving the ball.
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	###Checking the border
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
		os.system("aplay bounce.wav&")

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
		os.system("aplay bounce.wav&")

	if ball.xcor() > 390:
		ball.goto(0,0)
		ball.dx *= -1
		os.system("aplay bounce.wav&")
	if ball.xcor() < -390:
		ball.goto(0,0)
		ball.dx *= -1
		os.system("aplay bounce.wav&")

	### Tuning the collisions of paddle and the ball.
	
	if ball.xcor() > 340 and ball.ycor() < pb.ycor() + 40 and ball.ycor() > pb.ycor() - 40 and ball.xcor() < 350:
		ball.setx(340)
		ball.dx *= -1
		sa+=1
		pen.clear()
		pen.write("Player 1 : {} \nPlayer 2 : {}".format(sa,sb),align = 'center',font = ("Courier",20,"normal"))		
		os.system("aplay bounce.wav&")

	if ball.xcor() < -340 and ball.ycor() < pa.ycor() + 40 and ball.ycor() > pa.ycor() - 40 and ball.xcor() > -350:
		ball.setx(-340)
		ball.dx *= -1
		sb+=1
		pen.clear()
		pen.write("Player 1 : {} \nPlayer 2 : {}".format(sa,sb),align = 'center',font = ("Courier",20,"normal"))	
		os.system("aplay bounce.wav&")