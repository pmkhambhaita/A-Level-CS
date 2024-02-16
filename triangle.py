import math, turtle, time

tess = turtle.Turtle()  # create an instance of an object of type Turtle
wn = turtle.Screen()  # create an instance of an object of type Screen

wn.bgcolor("White")  # background color
wn.tracer(12)  # render only every 12th frame - increases animation speed
tess.speed(9)  # max draw speed
tess.color("BlueViolet")  # linecolor

def drawTriangle(leftCorner, sideLength, clr):
    # Draw a triagle with given position of left corner,
    # length of a side and line color.
    x, y = leftCorner[0], leftCorner[1]
    tess.color(clr)
    tess.penup()
    tess.goto(x, y)
    tess.pendown()
    tess.goto(x + sideLength / 2, y + math.sqrt(3) * sideLength / 2)
    tess.goto(x + sideLength, y)
    tess.goto(x, y)
    tess.penup()

def serpTri(leftCorner = (-150, -100), sideLength = 400, depth = 6, color = "blue"):
    if depth == 0:  # maximum recursion depth achieved
        return
    drawTriangle(leftCorner, sideLength, color)
    mdptLeft = (leftCorner[0] + sideLength / 4, leftCorner[1] + sideLength * math.sqrt(3) / 4)
    mdptBottom = (leftCorner[0] + sideLength / 2, leftCorner[1])
    # In each resursive call, depth is decreased by 1.
    # When depth reaches 0, the recurion ends.
    serpTri(leftCorner, sideLength/2, depth-1)
    serpTri(mdptLeft, sideLength/2, depth-1)
    serpTri(mdptBottom, sideLength/2, depth-1)

sideLength = 200
maxDepth = 6

for d in range(1, maxDepth + 1):
    # coordinates of left corner, then side length,
    # then recursion depth
    serpTri((-150, -100), sideLength, d)
    wn.update()  # Uncomment if a tracer has been set
    time.sleep(2)
    tess.clear()

# perform final update
wn.update()
# keep the window open
turtle.done()