def binary_search(arr, low, high, x):
    print("Start: ")
    for index in range(low, high + 1):
        print(arr[index], end=" ")
    print("\n")
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

arr = [2, 3, 4, 10, 40]
x = 10

result = binary_search(arr, 0, len(arr) - 1, x)

print("\nElement is present at index %d" % result)