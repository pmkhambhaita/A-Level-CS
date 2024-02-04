import math

def factorialNo(n):
    if n == 0:       # base case
        return 1
    else:         # recursive case          
        return n * factorialNo(n - 1)
    
print(factorialNo(5)) 

print("Expected: " + str(math.factorial(5)))