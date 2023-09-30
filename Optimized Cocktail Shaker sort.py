import random
import time


def optimized_cocktail_shaker_sort(arr):
    n = len(arr)
    # Initialize start and end indices
    start = 0
    end = n-1
    while start < end:
        # Move largest element to end
        last_swapped = start
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                last_swapped = i
        end = last_swapped
        # If no swaps were made, the array is already sorted
        if start >= end:
            break
        # Move smallest element to start
        last_swapped = end
        for i in range(end-1, start-1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                last_swapped = i
        start = last_swapped
    return arr


# Generate a random array of length 10 with values between 1 and 100
arr = [random.randint(0, 1000) for _ in range(10000)]

# Sort the array using bubble sort and measure the time taken
startTime = time.time()
optimized_cocktail_shaker_sort(arr)
endTime = time.time()

# Print the time to sort array
print(f"Time taken: {endTime - startTime}")
