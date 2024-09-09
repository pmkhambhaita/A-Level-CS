import time
A = 253
r = 12
C = A/r

while abs(A - r) >= 0.01:
    r = (r + A / r) / 2
    print(r)
    time.sleep(1)