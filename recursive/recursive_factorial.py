import math

def factorialNo(n):
    if n == 1:       # base case
        return n
    else:         # recursive case          
        return n * factorialNo(n - 1)
    
print(factorialNo(5)) 

print("Expected: " + str(math.factorial(5)))

'''

TRACE
---------------------
factorialNo(4)
else case
return 4 * factorialNo(3) == 4 * 6 == **24** ⤣ (return to user)
    ---------------------
    factorialNo(3)
    else case
    return 3 * factorialNo(2) == 3 * 2 == 6 ⤣
        ---------------------
        factorialNo(2)
        else case
        return 2 * factorialNo(1) == 2 * 1 == 2 ⤣
            ---------------------
            factorialNo(1)
            1 == 1
            return 1 ⤣
''' 