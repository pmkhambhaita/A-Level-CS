def recursive_subtract_add(value, subtract=True):
    if value <= 0:
        if value == 0:
            print(value)
        return
    print(value)
    next_value = value - 2 if subtract else value + 1
    recursive_subtract_add(next_value, not subtract)


# Example usage
initial_value = int(input("Enter an integer: "))
recursive_subtract_add(initial_value)


def iterative_subtract_add(value):
    subtract = True
    while value > 0:
        print(value)
        value = value - 2 if subtract else value + 1
        subtract = not subtract
    if value == 0:
        print(value)


# Example usage
initial_value = int(input("Enter an integer: "))
iterative_subtract_add(initial_value)