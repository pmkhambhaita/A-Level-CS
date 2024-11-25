def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any elements were swapped in this pass
        swapped = False
        print(f"Pass {i+1}:")
        for j in range(0, n-i-1):
            print(f"  Comparing {arr[j]} and {arr[j+1]}")
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print(f"  Swapped {arr[j]} and {arr[j+1]}")
            else:
                print(f"  No swap needed")
        # Print the array after each pass
        print(f"Array after pass {i+1}: {arr}")
        # If no elements were swapped, the array is sorted
        if not swapped:
            break

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    bubble_sort(arr)
    print("Sorted array:", arr)