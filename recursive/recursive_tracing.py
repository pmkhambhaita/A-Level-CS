def myCode(x):
    if x < 1:
        return
    else:
        print(x)
        myCode(x - 3)

myCode(10)

'''
TRACE
---------------------
myCode(10)
10 > 1
print(10)
myCode(10-3) -> 7
---------------------
myCode(7)
7 > 1
print(7)
myCode(7-3) -> 4
---------------------
myCode(4)
4 > 1
print(4)
myCode(4-3) -> 1
---------------------
myCode(1)   
1 = 1
print(1)
myCode(1-3) -> -2
---------------------
myCode(-2)
-2 < 1
return

'''
