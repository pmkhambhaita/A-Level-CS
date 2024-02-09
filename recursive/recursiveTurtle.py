import turtle
t = turtle.Turtle()
window = turtle.Screen()

colours = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']

t.pendown()
def square(size):
    if size <= 5:
        return
    else:
        t.color(colours[(size//10) % len(colours)])
        for i in range(4):
            t.forward(size)
            t.right(90)
        square(size - 10)

square(100)

window.exitonclick()