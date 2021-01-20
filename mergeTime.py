import random
import time

# Reference for merge sort :  https://www.geeksforgeeks.org/merge-sort/
def merge_sort(array_list):
    """ this function implements a merge sort to sort an array/vector of integers in ascending order"""
    if len(array_list) > 1:
        # locate the middle point of array
        mid_array = len(array_list) // 2
        # split the array into 2 halves (defined by left and right half)
        left_half = array_list[:mid_array]
        right_half = array_list[mid_array:]
        # call merge sort to sort the left half
        merge_sort(left_half)
        # call merge sort to sort the right half
        merge_sort(right_half)

        i = j = k = 0
        # merge sort: divide and conquer method
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array_list[k] = left_half[i]
                i += 1
            else:
                array_list[k] = right_half[j]
                j += 1
            k += 1

        # check to see if any elements were left
        while i < len(left_half):
            array_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array_list[k] = right_half[j]
            j += 1
            k += 1

# Record running times for n = 5000, 10000, 15000, 20,000, 25,000, 30,000, 35,000
# Random integer values from -10,000 to 10,000
n= 5000
array = []
start = time.time()
for i in range(n):
    array.append(random.randint(-10000,10000))
merge_sort(array)
end = time.time()
print('Array size n = 5,000   Time: ', end-start)

n= 10000
array = []
start = time.time()
for i in range(n):
    array.append(random.randint(-10000,10000))
merge_sort(array)
end = time.time()
print('Array size n = 10,000   Time: ', end-start)

n= 15000
array = []
start = time.time()
for i in range(n):
    array.append(random.randint(-10000,10000))
merge_sort(array)
end = time.time()
print('Array size n = 15,000   Time: ', end-start)

n= 20000
array = []
start = time.time()
for i in range(n):
    array.append(random.randint(-10000,10000))
merge_sort(array)
end = time.time()
print('Array size n = 20,000   Time: ', end-start)

n= 25000
array = []
start = time.time()
for i in range(n):
    array.append(random.randint(-10000,10000))
merge_sort(array)
end = time.time()
print('Array size n = 25,000   Time: ', end-start)

n= 30000
array = []
start = time.time()
for i in range(n):
    array.append(random.randint(-10000,10000))
merge_sort(array)
end = time.time()
print('Array size n = 30,000   Time: ', end-start)


n= 35000
array = []
start = time.time()
for i in range(n):
    array.append(random.randint(-10000,10000))
merge_sort(array)
end = time.time()
print('Array size n = 35,000   Time: ', end-start)
