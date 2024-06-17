#number = int(input("Enter a number: "))
#print("Too low" if number < 1 else "Too high" if number > 9 else "Valid")

number = int(input("Enter a number: "))
print('Valid' if 1 <= number <= 9 else 'Invalid')