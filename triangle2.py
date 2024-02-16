import turtle

import os

myStack = ['', '', '']
topPointer = -1         # Create pointer and stack
def push(data):
    global topPointer
    if topPointer == len(myStack) - 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Stack Overflow')
        return
    else:
        topPointer += 1
        myStack[topPointer] = data
def pop():
    global topPointer
    if topPointer == -1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Stack Underflow\n')
        return
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Stack size before: ' + str(topPointer + 1) + '\n')
        topPointer -= 1
        print('Data popped: ' + myStack[topPointer + 1] + '\n')
        myStack[topPointer + 1] = ''
        print('Stack size after: ' + str(topPointer + 1) + '\n')
        return myStack[topPointer + 1]
def peek():
    global topPointer
    if topPointer == -1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Stack Underflow\n')
        return
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(myStack[topPointer])

def printStack():
    global topPointer
    if topPointer == -1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Stack is empty\n')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n<--- BOTTOM-----------TOP--->\n")
        print('\nStack: ', end="")
        for i in range(len(myStack)):
            print(myStack[i] + " ", end="")
        print()

def main():
    while True:
        print('\nEnter ps to print stack')
        print('Enter e to exit')
        print('Enter push to push data into stack')
        print('Enter pop to pop data from stack')
        print('Enter peek to peek at data from stack\n')

        command = input('Enter command: ')
        if command.lower() == 'ps':
            os.system('cls' if os.name == 'nt' else 'clear')
            printStack()
        elif command.lower() == 'e':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif command.lower() == 'push':
            os.system('cls' if os.name == 'nt' else 'clear')
            data = input('Enter data to push: ')
            push(data)
            print(data + ' added to stack\n')
        elif command.lower() == 'pop':
            os.system('cls' if os.name == 'nt' else 'clear')
            pop()
        elif command.lower() == 'peek':
            os.system('cls' if os.name == 'nt' else 'clear')
            peek()


#### TRIANGLE RECURSION ####




def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()


def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree, myTurtle):
    push('sierpinski')
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0],
                    getMid(points[0], points[1]),
                    getMid(points[0], points[2])],
                   degree-1, myTurtle)
        pop()
        sierpinski([points[1],
                    getMid(points[0], points[1]),
                    getMid(points[1], points[2])],
                   degree-1, myTurtle)
        pop()
        sierpinski([points[2],
                    getMid(points[2], points[1]),
                    getMid(points[0], points[2])],
                   degree-1, myTurtle)
        pop()


def main_recur():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myTurtle.speed(1)
    myPoints = [[-100, -50], [0, 100], [100, -50]]
    sierpinski(myPoints, 3, myTurtle)
    myWin.exitonclick()

main_recur()
