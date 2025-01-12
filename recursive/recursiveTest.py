"""

def doStuff(x):
    print("doStuff: ", x)
    if x <= 0:
        print("**return**")
        return
    print("no return")
    print(x)
    return doStuff(x-2)

doStuff(10)
"""

"""
TRACE
---------------------
doStuff(10)
10 > 0
print(10)
doStuff(10-2) -> 8
---------------------
⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
---------------------
doStuff(8)
8 > 0
print(8)
doStuff(8-2) -> 6
---------------------
⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
---------------------
doStuff(6)
6 > 0
print(6)
doStuff(6-2) -> 4
---------------------
⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
---------------------
doStuff(4)
4 > 0
print(4)
doStuff(4-2) -> 2
---------------------
⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
---------------------
doStuff(2)
2 > 0
print(2)
doStuff(2-2) -> 0
---------------------
⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
---------------------
doStuff(0)
0 <= 0
**return**
---------------------
"""
def doStuff(x):
    if x > 10:
        return
    
    print(x)
    doStuff(x+2)

doStuff(2)

"""
TRACE
---------------------
doStuff(2)
2 < 10
print(2)
doStuff(2+2) -> 4
---------------------
⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
---------------------
doStuff(4)
4 < 10
print(4)
doStuff(4+2) -> 6
---------------------
⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
---------------------
doStuff(6)  
6 < 10
print(6)
doStuff(6+2) -> 8
---------------------
⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
---------------------
doStuff(8)
8 < 10
print(8)
doStuff(8+2) -> 10
---------------------
⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
---------------------
doStuff(10)
10 = 10
print(10)
doStuff(10+2) -> 12
---------------------
⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
---------------------
doStuff(12)
12 > 10
**return**
---------------------

"""


"""
| Recursion is a way of solving problems in which a function calls itself as a subroutine.
| This allows the function to be repeated several times, since it calls itself during its execution.
| Recursive subroutines should contain a condition that stops the recursion and is reachable within a finite number of steps.
| This condition is called the base case.
| If this is not implemented, the recursion will continue until the program crashes due to a stack overflow.
"""