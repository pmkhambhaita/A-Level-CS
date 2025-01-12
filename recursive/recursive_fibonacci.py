def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(9))

"""
### TRACE ###
fibonacci(9)
9 != 0 and 9 != 1 and 9 != 2
fibonacci((9-1) + fibonacci(9-2))
    fibonacci(8)
    8 != 0 and 8 != 1 and 8 != 2
    fibonacci((8-1) + fibonacci(8-2))
        fibonacci(7)
        7 != 0 and 7 != 1 and 7 != 2
        fibonacci((7-1) + fibonacci(7-2))
            fibonacci(6)
            6 != 0 and 6 != 1 and 6 != 2
            fibonacci((6-1) + fibonacci(6-2))
                fibonacci(5)
                5 != 0 and 5 != 1 and 5 != 2
                fibonacci((5-1) + fibonacci(5-2))
                    fibonacci(4)
                    4 != 0 and 4 != 1 and 4 != 2
                    fibonacci((4-1) + fibonacci(4-2))
                        fibonacci(3)
                        3 != 0 and 3 != 1 and 3 != 2
                        fibonacci((3-1) + fibonacci(3-2))
                            fibonacci(2)
                            return 1   
                            fibonacci(1)
                            return 1 
                        return 2
                    return 3
                return 5
            return 8
        return 13
    return 21
return 34
        
"""