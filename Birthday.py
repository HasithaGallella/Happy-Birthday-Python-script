#Black Gale productions
#@H.B.Gallella
import turtle
import random
import time
bg = turtle.Screen()
bg.bgcolor("black")
#Line layer function
def layer(x,y,l,h,col,bgcol):
    turtle.penup()
    turtle.goto(x,y)
    turtle.color(col)
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(h)
    turtle.end_fill()
    bg.bgcolor(bgcol)
    turtle.penup()
    turtle.home()
# Bottom Line 1
layer(-160,-280,260,40,"pink","lightblue")
# Mid Line 2
layer(-140,-240,220,60,"white","blue")
# First Line 3
layer(-120,-180,180,80,"pink","violet")
# Cake
turtle.goto(-100,-100)
turtle.color("white")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()
bg.bgcolor("red")
# Candles
turtle.pensize(7)
turtle.penup()
turtle.goto(-90,0)
turtle.color("yellow")
turtle.left(180)
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(-60,0)
turtle.color("pink")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(-30,0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(0,0)
turtle.color("pink")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(30,0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)
bg.bgcolor("black")
# Decoration
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-40,-50)
turtle.pendown()
#MMM
for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)
#MMM
bg.bgcolor("black")
#2nd part
turtle.penup()
turtle.setpos(-50, 70)
turtle.color("pink")
turtle.pendown()
turtle.write(arg=f"Happy Birthday 'Name' !!!", align="center", font=("jokerman", 30, "italic"))
time.sleep(1)
#copyright block
turtle.bgcolor("black")
time.sleep(0.2)
turtle.bgcolor("blue")
time.sleep(0.2)
turtle.bgcolor("violet")
time.sleep(0.2)
turtle.bgcolor("red")
time.sleep(0.2)
turtle.bgcolor("yellow")
time.sleep(0.2)
turtle.bgcolor("white")
time.sleep(0.2)
turtle.bgcolor("black")
time.sleep(3)
turtle.reset()
#MMM
turtle.speed(100)
turtle.bgcolor("black")
#MMM
for i in range(150):
 turtle.color("cyan")
 turtle.circle(i)
 turtle.left(10)
#bicc
turtle.penup()
turtle.home()
turtle.left(200)
turtle.pendown()
#anfd 
turtle.color("pink")
turtle.write(' Yours  loving  Hasitha :) ', move=False, align='center',font=('Arial',40, 'bold'))
for i in range(150,190):
 turtle.color("cyan")
 turtle.circle(i)
 turtle.left(10)
#end
turtle.done()