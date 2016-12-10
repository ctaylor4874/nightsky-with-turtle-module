import turtle
from random import randint;

#set background color
turtle.bgcolor('#00050a')

#set turtle speed
turtle.speed(7)

#hide turtle from view
turtle.hideturtle()

#draw outer circle to create color fade
def outCircle2(size):
    turtle.pencolor('#00050a')
    turtle.color("#fafad1")
    turtle.up()
    turtle.home()
    moonCords = (-250, -250)
    x,y = moonCords
    turtle.forward(x)
    turtle.setheading(270)
    turtle.forward(y)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(size + 10)
    turtle.end_fill()

#draw outer circle to create color fade
def outCircle3(size):
    turtle.pencolor('#f7f7bb')
    turtle.color("#f7f7bb")
    turtle.up()
    turtle.home()
    moonCords = (-250, -250)
    x,y = moonCords
    turtle.forward(x)
    turtle.setheading(270)
    turtle.forward(y)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(size + 5)
    turtle.end_fill()

#draw moon circle
def circle(size):
    turtle.pencolor('#f4f4a4')
    turtle.color("#f4f4a4")
    turtle.up()
    turtle.home()
    moonCords = (-250, -250)
    x,y = moonCords
    turtle.forward(x)
    turtle.setheading(270)
    turtle.forward(y)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

#call circles to draw moon
def draw_moon():
    outCircle2(50)
    outCircle3(50)
    circle(50)

#draw small stars at random points on screen
def smallStar():
    widthWin = ((turtle.window_width()) / 2)
    heightWin = ((turtle.window_height()) / 2)
    turtle.setheading(0)
    turtle.pencolor('#f4f4a4')
    randCor1 = randint(-(widthWin), widthWin)
    randCor2 = randint(-(heightWin), heightWin)
    cords = (randCor1, randCor2)
    randHead = randint(1, 360)
    turtle.up()
    turtle.home()
    x,y = cords
    turtle.forward(x)
    turtle.setheading(270)
    turtle.forward(y)
    turtle.down()
    # turtle.color('white')
    turtle.begin_fill()
    starSize = (randint(1,2))
    for i in xrange(5):
        turtle.right(144)
        turtle.forward(starSize)
        turtle.end_fill()

#draw bigger stars at random points on screen
def bigStar():
    widthWin = ((turtle.window_width()) / 2)
    heightWin = ((turtle.window_height()) / 2)
    turtle.setheading(0)
    turtle.pencolor('#f4f4a4')
    randCor1 = randint(-(widthWin), widthWin)
    randCor2 = randint(-(heightWin), heightWin)
    cords = (randCor1, randCor2)
    randHead = randint(1, 360)
    turtle.up()
    turtle.home()
    x,y = cords
    turtle.forward(x)
    turtle.setheading(270)
    turtle.forward(y)
    turtle.down()
    turtle.begin_fill()
    starSize = (randint(3, 6))
    for i in xrange(5):
        turtle.right(144)
        turtle.forward(starSize)
        turtle.end_fill()

##################################
#call functions to draw moon
draw_moon()
#draw stars
for stars in xrange(1, 1000):
    #draw small stars
    for i in xrange(1, 50):
        smallStar()
    #draw big stars
    for n in xrange(1, 5):
        bigStar()


turtle.mainloop()
