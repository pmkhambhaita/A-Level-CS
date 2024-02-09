import turtle
t = turtle.Turtle()
window = turtle.Screen()

def square(size):
    if size > 5:
        return
    else:
        for i in range(4):
            t.forward(size)
            t.right(90)
        square(size - 10)

square(400)

window.exitonclick()