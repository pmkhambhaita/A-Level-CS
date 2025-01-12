import turtle
window = turtle.Screen()
t = turtle.Turtle()

def draw_square(colour, size):
    t.color(colour)
    for i in range(4):
        t.forward(size)
        t.left(90)


draw_square("red", 50) # draw a red square of size 50
draw_square("blue", 150) # draw a blue square of size 100
draw_square("green", 100) # draw a green square of size 150


window.exitonclick()

