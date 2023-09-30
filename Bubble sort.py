import random
import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# Generate a random array of length 10 with values between 1 and 100
arr1 = [random.randint(0, 1000) for _ in range(10000)]
arr2 = [random.randint(0, 1000) for _ in range(10000)]

# Sort the array using bubble sort and measure the time taken
startTime = time.time()
bubble_sort(arr1)
endTime = time.time()

# Print the time to sort array
print(f"Time taken: {endTime - startTime}")
