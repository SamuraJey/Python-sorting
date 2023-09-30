import random
import time


def optimized_bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Flag to detect if any swap is made in this iteration
        swapped = False
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr


# Generate a random array of length 10 with values between 1 and 100
arr = [random.randint(0, 1000) for _ in range(10000)]

# Sort the array using bubble sort and measure the time taken
startTime = time.time()
optimized_bubble_sort(arr)
endTime = time.time()

# Print the time to sort array
print(f"Time taken: {endTime - startTime}")
