def asciiAdd(inp_str):
    total = 0
    for char in inp_str:
        total += ord(char)
    return total

inp_str = input("Enter a string: ")

print(asciiAdd(inp_str))
