import random
import time


def gnome_sort(arr):
    n = len(arr)
    pos = 0
    while pos < n:
        if pos == 0 or arr[pos] >= arr[pos-1]:
            pos += 1
        else:
            arr[pos], arr[pos-1] = arr[pos-1], arr[pos]
            pos -= 1
    return arr


# Generate a random array of length 10 with values between 1 and 100
arr = [random.randint(0, 1000) for _ in range(10000)]

# Sort the array using bubble sort and measure the time taken
startTime = time.time()
gnome_sort(arr)
endTime = time.time()

# Print the time to sort array
print(f"Time taken: {endTime - startTime}")
# It`s kinda bad.
