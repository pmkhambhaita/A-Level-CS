"""

string1 = input("Enter a string: ")
string2 = input("Enter another string: ")

bigString = string1 + string2

print(bigString)

number = int(input("Enter a number: "))

def checkNumber():
    if number < 0 or number > 9:
        print("Error")
    else:
        print("OK")

checkNumber()

pswd = input("Enter a password: ")

def lenCheck():
    if len(pswd) < 8:
        print("Error")
    else:
        print("OK")

lenCheck()

import random

target = random.randint(1, 9)
number = int(input("Enter a number: "))
def randomNum():
    if target == number:
        print("Correct")
    if target < number:
        print("Too high")
    if target > number:
        print("Too low")

randomNum()

"""

students = [
    ['Bill', 12, 23],
    ['Tom', 14, 13],
    ['Amy', 17, 18]
]

for i in range(0, 3):
    print(students[i][0], end=" ")
    print(students[i][1], end=" ")
    print(students[i][2], end=" ")
    print("\n")

tom = students[1]
print(tom)