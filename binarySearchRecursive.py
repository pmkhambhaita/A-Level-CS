def binary_search(arr, low, high, x):
    print("Start: ")
    for index in range(low, high + 1):
        print(arr[index], end=" ")
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

binary_search([2, 3, 4, 10, 40], 0, 4, 10)