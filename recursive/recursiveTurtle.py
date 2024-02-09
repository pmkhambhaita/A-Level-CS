import turtle
t = turtle.Turtle()
window = turtle.Screen()

colours = ['red', 'green']

t.pendown()
def square(size):
    if size <= 5:
        return
    else:
        t.color(colours[(size//10) % 2])
        for i in range(4):
            t.forward(size)
            t.right(90)
        square(size - 10)

square(100)

window.exitonclick()