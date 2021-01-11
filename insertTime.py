import random
import time

# Reference: Insertion Sort method implemented from CS162 Lecture (Exploration:Searching,sorting,algorithm analysis)
def insert_sort(array_list):
    """ this function will sort a given vector/array of integers in ascending order"""
    # the second value from the array is pulled, values larger than value pulled is slided over, value pulled fills spot
    for index in range(1, len(array_list)):
        val = array_list[index]
        j = index - 1
        # iterate through the array until all values are sorted in correct position
        while j >= 0 and array_list[j] > val:
            array_list[j + 1] = array_list[j]
            j -= 1
        array_list[j + 1] = val

# Record running times for n = 5000, 10000, 15000, 20,000, 25,000, 30,000, 35,000
# Random integer values from -10,000 to 10,000
n= 5000
array = []
start = time.time()
for i in range(n):
    array.append(random.randint(-10000,10000))
insert_sort(array)
end = time.time()
print('Array size n = 5,000   Time: ', end-start)

n= 10000
array = []
start = time.time()
for i in range(n):
    array.append(random.randint(-10000,10000))
insert_sort(array)
end = time.time()
print('Array size n = 10,000   Time: ', end-start)

n= 15000
array = []
start = time.time()
for i in range(n):
    array.append(random.randint(-10000,10000))
insert_sort(array)
end = time.time()
print('Array size n = 15,000   Time: ', end-start)

n= 20000
array = []
start = time.time()
for i in range(n):
    array.append(random.randint(-10000,10000))
insert_sort(array)
end = time.time()
print('Array size n = 20,000   Time: ', end-start)

n= 25000
array = []
start = time.time()
for i in range(n):
    array.append(random.randint(-10000,10000))
insert_sort(array)
end = time.time()
print('Array size n = 25,000   Time: ', end-start)

n= 30000
array = []
start = time.time()
for i in range(n):
    array.append(random.randint(-10000,10000))
insert_sort(array)
end = time.time()
print('Array size n = 30,000   Time: ', end-start)


n= 35000
array = []
start = time.time()
for i in range(n):
    array.append(random.randint(-10000,10000))
insert_sort(array)
end = time.time()
print('Array size n = 35,000   Time: ', end-start)
