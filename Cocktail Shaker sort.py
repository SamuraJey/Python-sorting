import random
import time


def cocktail_shaker_sort(arr):
    n = len(arr)
    # Initialize swapped to True to enter the loop
    swapped = True
    # Initialize start and end indices
    start = 0
    end = n-1
    while swapped:
        # Reset swapped to False
        swapped = False
        # Move largest element to end
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        # If no swaps were made, the array is already sorted
        if not swapped:
            break
        # Move smallest element to start
        swapped = False
        end -= 1
        for i in range(end-1, start-1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        start += 1
    return arr


# Generate a random array of length 10 with values between 1 and 100
arr = [random.randint(0, 1000) for _ in range(10000)]

# Sort the array using bubble sort and measure the time taken
startTime = time.time()
cocktail_shaker_sort(arr)
endTime = time.time()

# Print the time to sort array
print(f"Time taken: {endTime - startTime}")
