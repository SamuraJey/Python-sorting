import random
import time


def circle_sort(arr):
    n = len(arr)
    is_swapped = True
    start = 0
    end = n - 1

    while is_swapped:
        is_swapped = False

        # Move the largest element to the end of the array
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_swapped = True

        if not is_swapped:
            break

        is_swapped = False

        # Move the smallest element to the beginning of the array
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_swapped = True

        start += 1
        end -= 1

    return arr


# Generate a random array of length 10 with values between 1 and 100
arr = [random.randint(0, 1000) for _ in range(10000)]
sample_arr = arr.copy()

# Sort the array using bubble sort and measure the time taken
startTime = time.time()
circle_sort(arr)
endTime = time.time()

# Print the time to sort array
print(f"Time taken: {endTime - startTime}")
sample_arr.sort()
assert arr == sample_arr, "Arrays are not equal"
print("The arrays are equal")
