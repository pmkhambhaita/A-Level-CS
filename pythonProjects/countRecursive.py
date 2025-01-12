def doStuff(x):
    if x <= 0:
        return
    else:
        print(x)
        doStuff(x - 2)

doStuff(10)