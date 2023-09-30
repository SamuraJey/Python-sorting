import random
import time


def comb_sort(arr):
    gap = len(arr)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1

    return arr


# Generate a random array of length 10 with values between 1 and 100
arr = [random.randint(0, 1000) for _ in range(10000)]
sample_arr = arr.copy()

# Sort the array using bubble sort and measure the time taken
startTime = time.time()
comb_sort(arr)
endTime = time.time()

# Print the time to sort array
print(f"Time taken: {endTime - startTime}")
sample_arr.sort()
assert arr == sample_arr, "Arrays are not equal"
print("The arrays are equal")
