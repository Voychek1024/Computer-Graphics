"""Read this before using the program!"""

# This program REQUIRES some extra things to work. These are MANDITORY.
# The code WILL NOT WORK without them. If you do not install them, it WILL
# NOT WORK, and that is your own fault! Please install them!

# That being said, these extra programs convert the turtle canvas into a
# PNG file for your own use. This will allow you to keep the circles somewhere
# handy. If you just want to demonstate

# Here are the required programs:

# 1. Latest version of Pillow by Alex Clark and Contributers. This is not
# required if you're not interested in saving finished images.

# 2. Latest version of Ghostscript by Artifex Software, Inc. This code uses
# version 9.27. This is not a python module but it is required to use
# Pillow's image saving features. You can download Ghostscript here:
# https://www.ghostscript.com/download/gsdnld.html

# If these programs are not installed, please ensure the variable "doNotPrint"
# is set to True. It's set to True by default. If these programs are installed,
# don't forget to update "doNotPrint" to False, otherwise the code will skip
# over the image saving process.

doNotPrint = False  # SET TO TRUE BY DEFAULT

"----------------------------------------------------------------------------"

"Initialization"

import time
import turtle
import math
from PIL import Image

start = time.time()
t = turtle.Turtle()

moveList1 = []
moveList2 = []
moveList3 = []
moveList4 = []

"----------------------------------------------------------------------------"

"Cardinal Directions"


def North(tile):
    l = tile
    t.setheading(90)
    t.forward(l)


def West(tile):
    l = tile
    t.setheading(180)
    t.forward(l)
    t.fillcolor("red")
    t.begin_fill()
    t.goto(t.pos() + (-l, 0))
    t.goto(t.pos() + (0, -l))
    t.goto(t.pos() + (l, 0))
    t.goto(t.pos() + (0, l))
    t.end_fill()


def South(tile):
    l = tile
    t.setheading(270)
    t.forward(l)


def East(tile):
    l = tile
    t.setheading(0)
    t.forward(l)
    t.begin_fill()
    t.goto(t.pos() + (l, 0))
    t.goto(t.pos() + (0, l))
    t.goto(t.pos() + (-l, 0))
    t.goto(t.pos() + (0, -l))
    t.end_fill()


"----------------------------------------------------------------------------"

"Drawing The Grid"


def gridDraw(width, height, tile):
    t.speed(0)
    x = width
    y = height
    l = tile
    t.penup()
    t.goto(-(x / 2) * l, -(y / 2) * l)
    t.pendown()
    WHY = 0
    for k in range(y + 1):
        t.forward(x * l)
        if WHY < y:
            WHY = WHY + 1
        else:
            WHY = WHY
        t.penup()
        t.goto(-(x / 2) * l, (-(y / 2) + WHY) * l)
        t.pendown()

    EX = 0
    t.right(90)
    t.penup()
    t.goto((-x / 2) * l, (((y / 2) * l)))
    t.pendown()

    for k in range(x + 1):
        t.forward(l * y)
        if EX < x:
            EX = EX + 1
        else:
            EX = EX
        t.penup()
        t.goto((((-x / 2) + EX) * l), ((y / 2) * l))
        t.pendown()

    t.penup()
    t.goto(0, 0)


"----------------------------------------------------------------------------"

"Cartesian Quadrants"


def Quad1(width, height, tile):
    global InQuad1, InQuad2, InQuad3, InQuad4
    InQuad1 = False
    InQuad2 = False
    InQuad3 = False
    InQuad4 = False
    t.penup()
    t.goto((0.5 * width * tile), 0)
    t.pendown()
    t.setheading(90)
    InQuad1 = True


def Quad2(width, height, tile):
    global InQuad1, InQuad2, InQuad3, InQuad4
    InQuad1 = False
    InQuad2 = False
    InQuad3 = False
    InQuad4 = False
    t.penup()
    t.goto((-0.5 * width * tile), 0)
    t.pendown()
    t.setheading(90)
    InQuad2 = True


def Quad3(width, height, tile):
    global InQuad1, InQuad2, InQuad3, InQuad4
    InQuad1 = False
    InQuad2 = False
    InQuad3 = False
    InQuad4 = False
    t.penup()
    t.goto(-0.5 * width * tile, 0)
    t.pendown()
    t.setheading(270)
    InQuad3 = True


def Quad4(width, height, tile):
    global InQuad1, InQuad2, InQuad3, InQuad4
    InQuad1 = False
    InQuad2 = False
    InQuad3 = False
    InQuad4 = False
    t.penup()
    t.goto(((0.5 * width * tile)), 0)
    t.pendown()
    t.setheading(270)
    InQuad4 = True


"----------------------------------------------------------------------------"

"Determining the Midpoint and Radius of Each Pixel"


def whatPixel(xCoord, yCoord, tile, width, height):
    l = tile
    global midMag, midX, midY

    if InQuad1 == True:
        midX = (xCoord / l) - 0.5
        midY = (yCoord / l) - 0.5

    if InQuad2 == True:
        midX = (xCoord / l) + 0.5
        midY = (yCoord / l) - 0.5

    if InQuad3 == True:
        midX = (xCoord / l) + 0.5
        midY = (yCoord / l) - 0.5

    if InQuad4 == True:
        midX = (xCoord / l) - 0.5
        midY = (yCoord / l) - 0.5

    midMag = (math.sqrt((midX ** 2) + (midY ** 2)))


def radCalc(xVal, width, height):
    global radius
    a = width
    b = height

    if a == b:
        radius = 0.5 * a
    else:
        print("Width must equal height. If you want to draw ellipses, you")
        print("can try finising the code yourself. Check line 216")

        # xComp=xVal
        # yComp=math.sqrt( (b**2)(1- ((xVal**2)/(a**2)) ) )
        # radius=math.sqrt((xComp**2)+(yComp**2))

        # A leftover from the ellipse calculation.


"----------------------------------------------------------------------------"

"Instructions for Shading The Grid, Per Quadrant"


def midpointQuad1(radius, midMag, xVal, width, height, tile):
    xCoord = t.xcor()
    yCoord = t.ycor()
    l = tile
    xVal = xCoord
    t.speed(0)

    if abs(radius) - abs(midMag) >= 0:
        t.fillcolor("red")
        t.begin_fill()
        t.goto(t.pos() + (-l, 0))
        t.goto(t.pos() + (0, -l))
        t.goto(t.pos() + (l, 0))
        t.goto(t.pos() + (0, l))
        t.end_fill()
        t.forward(l)
        xCoord = t.xcor()
        yCoord = t.ycor()
        xVal = xCoord
        whatPixel(xCoord, yCoord, tile, width, height)
        radCalc(xVal, width, height)
        moveList1.append("West(tile)")

    if abs(radius) - abs(midMag) < 0:
        t.left(90)
        t.forward(l)
        t.fillcolor("red")
        t.begin_fill()
        t.goto(t.pos() + (-l, 0))
        t.goto(t.pos() + (0, -l))
        t.goto(t.pos() + (l, 0))
        t.goto(t.pos() + (0, l))
        t.end_fill()
        t.setheading(90)
        xCoord = t.xcor()
        yCoord = t.ycor()
        xVal = xCoord
        whatPixel(xCoord, yCoord, tile, width, height)
        radCalc(xVal, width, height)
        moveList1.append("North(tile)")


def midpointQuad2(radius, midMag, xVal, width, height, tile):
    xCoord = t.xcor()
    yCoord = t.ycor()
    l = tile
    xVal = xCoord
    t.speed(0)

    if abs(radius) - abs(midMag) >= 0:
        t.fillcolor("red")
        t.begin_fill()
        t.goto(t.pos() + (l, 0))
        t.goto(t.pos() + (0, -l))
        t.goto(t.pos() + (-l, 0))
        t.goto(t.pos() + (0, 2 * l))
        t.end_fill()
        xCoord = t.xcor()
        yCoord = t.ycor()
        xVal = xCoord
        whatPixel(xCoord, yCoord, tile, width, height)
        radCalc(xVal, width, height)
        moveList2.append("East(tile)")

    if abs(radius) - abs(midMag) < 0:
        t.right(90)
        t.forward(l)
        t.fillcolor("red")
        t.begin_fill()
        t.goto(t.pos() + (l, 0))
        t.goto(t.pos() + (0, -l))
        t.goto(t.pos() + (-l, 0))
        t.goto(t.pos() + (0, l))
        t.end_fill()
        t.setheading(90)
        xCoord = t.xcor()
        yCoord = t.ycor()
        xVal = xCoord
        whatPixel(xCoord, yCoord, tile, width, height)
        radCalc(xVal, width, height)
        moveList2.append("North(tile)")


def midpointQuad3(radius, midMag, xVal, width, height, tile):
    xCoord = t.xcor()
    yCoord = t.ycor()
    l = tile
    xVal = xCoord
    t.speed(0)

    if abs(radius) - abs(midMag) >= 0:
        t.fillcolor("red")
        t.begin_fill()
        t.goto(t.pos() + (l, 0))
        t.goto(t.pos() + (0, -l))
        t.goto(t.pos() + (-l, 0))
        t.goto(t.pos() + (0, l))
        t.end_fill()
        t.forward(l)
        xCoord = t.xcor()
        yCoord = t.ycor()
        xVal = xCoord
        whatPixel(xCoord, yCoord, tile, width, height)
        radCalc(xVal, width, height)
        moveList3.append("East(tile)")

    if abs(radius) - abs(midMag) < 0:
        t.left(90)
        t.forward(l)
        t.fillcolor("red")
        t.begin_fill()
        t.goto(t.pos() + (l, 0))
        t.goto(t.pos() + (0, -l))
        t.goto(t.pos() + (-l, 0))
        t.goto(t.pos() + (0, l))
        t.end_fill()
        t.setheading(270)
        xCoord = t.xcor()
        yCoord = t.ycor()
        xVal = xCoord
        whatPixel(xCoord, yCoord, tile, width, height)
        radCalc(xVal, width, height)
        moveList3.append("South(tile)")


def midpointQuad4(radius, midMag, xVal, width, height, tile):
    xCoord = t.xcor()
    yCoord = t.ycor()
    l = tile
    xVal = xCoord
    t.speed(0)

    if abs(radius) - abs(midMag) >= 0:
        t.setheading(270)
        t.fillcolor("red")
        t.begin_fill()
        t.goto(t.pos() - (l, 0))
        t.goto(t.pos() + (0, -l))
        t.goto(t.pos() + (l, 0))
        t.goto(t.pos() + (0, l))
        t.end_fill()
        t.forward(l)
        xCoord = t.xcor()
        yCoord = t.ycor()
        xVal = xCoord
        whatPixel(xCoord, yCoord, tile, width, height)
        radCalc(xVal, width, height)
        moveList4.append("West(tile)")

    if abs(radius) - abs(midMag) < 0:
        t.right(90)
        t.forward(l)
        t.fillcolor("red")
        t.begin_fill()
        t.goto(t.pos() + (-l, 0))
        t.goto(t.pos() + (0, -l))
        t.goto(t.pos() + (l, 0))
        t.goto(t.pos() + (0, l))
        t.end_fill()
        t.setheading(270)
        xCoord = t.xcor()
        yCoord = t.ycor()
        xVal = xCoord
        whatPixel(xCoord, yCoord, tile, width, height)
        radCalc(xVal, width, height)
        moveList4.append("South(tile)")


"----------------------------------------------------------------------------"

"Constructing The Circle"


def bresenham(width, height, tile):
    xCoord = t.xcor()
    yCoord = t.ycor()
    l = tile
    xVal = xCoord
    t.speed(0)

    Quad1(width, height, tile)

    print(("In Quad 1=" + str(InQuad1)))
    if height % 2 != 0:
        print("Odd")
        t.setheading(90)
        t.forward(0.5 * l)
    whatPixel(xCoord, yCoord, tile, width, height)
    radCalc(xVal, width, height)
    midpointQuad1(radius, midMag, xVal, width, height, tile)
    xCoord = t.xcor()
    while (midX != midY):
        xCoord = t.xcor()
        midpointQuad1(radius, midMag, xVal, width, height, tile)
    while len(moveList1) > 0:
        eval(moveList1.pop())
    print("Quad 1 complete")
    print(" ")

    Quad2(width, height, tile)

    if height % 2 != 0:
        print("Odd")
        t.setheading(90)
        t.forward(0.5 * l)
    print(("In Quad 2=" + str(InQuad2)))
    whatPixel(xCoord, yCoord, tile, width, height)
    radCalc(xVal, width, height)
    midpointQuad2(radius, midMag, xVal, width, height, tile)
    xCoord = t.xcor()
    while (abs(midX) != abs(midY)):
        xCoord = t.xcor()
        midpointQuad2(radius, midMag, xVal, width, height, tile)
    t.penup()
    t.goto(t.pos() + (0, -l))
    t.pendown()
    while len(moveList2) > 0:
        eval(moveList2.pop())
    East(tile)
    print("Quad 2 complete")
    print(" ")

    Quad3(width, height, tile)

    if height % 2 != 0:
        print("Odd")
        t.setheading(270)
        t.forward(0.5 * l)
    print(("In Quad 3=" + str(InQuad3)))
    whatPixel(xCoord, yCoord, tile, width, height)
    radCalc(xVal, width, height)
    midpointQuad3(radius, midMag, xVal, width, height, tile)
    xCoord = t.xcor()
    while (abs(midX) != abs(midY)):
        xCoord = t.xcor()
        midpointQuad3(radius, midMag, xVal, width, height, tile)
    t.penup()
    t.goto(t.pos() + (0, -l))
    t.pendown()

    while len(moveList3) > 0:
        eval(moveList3.pop())
    print("Quad 3 complete")
    print(" ")

    Quad4(width, height, tile)

    if height % 2 != 0:
        print("Odd")
        t.setheading(270)
        t.forward(0.5 * l)

    print(("In Quad 4=" + str(InQuad4)))
    print(" ")
    whatPixel(xCoord, yCoord, tile, width, height)
    radCalc(xVal, width, height)

    midpointQuad4(radius, midMag, xVal, width, height, tile)
    xCoord = t.xcor()
    while (abs(midX) != abs(midY)):
        xCoord = t.xcor()
        midpointQuad4(radius, midMag, xVal, width, height, tile)

    while len(moveList4) > 0:
        eval(moveList4.pop())
    West(tile)
    print("Quad 4 complete")


"----------------------------------------------------------------------------"

"Storing Your Image"


def imageStore(width, height):
    if doNotPrint == True:
        pass
    if doNotPrint == False:
        ts = turtle.getscreen()
        ts.getcanvas().postscript(file="Ellipse.eps")
        fileName = "Ellipse.eps"
        outputName = str(width) + "x" + str(height) + "Ellipse.png"
        outputFile = '{}'.format(outputName)
        image = Image.open(fileName)
        image.save(outputFile)


# The imageStore function was inspired by this article on stackoverflow.com.
# I've shortened the link so that it can fit in the text window.

# https://bit.ly/2VbmN1s
"----------------------------------------------------------------------------"


def allInOne(t, width, height, tile):
    gridDraw(width, height, tile)
    bresenham(width, height, tile)
    # imageStore(width, height)
    print("")
    print("Time Ellapsed: " + str('%.2f' % float(time.time() - start)) + " seconds")


# Use allInOne to run the code. The arguments are allInOne(t,width,height,tile)
# t -> Just enter the letter t, it controls the turtle module
# width -> Enter a whole number
# height -> Enter the same value you entered for width
# tile -> Controls the size of each grid tile. Recommended values: 10-40

allInOne(t, 35, 35, 20)
# This will create a circle on a 35x35 grid with a tile width of 20 pixels
